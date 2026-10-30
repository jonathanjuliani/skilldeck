#!/bin/bash
# Reproduce the eval. Usage: ./evals/run.sh <workdir> [model]
# Requires: claude CLI, node 22+ (fixtures use node:test, nothing to install).
set -u
WORK="${1:?usage: run.sh <workdir> [model]}"; MODEL="${2:-haiku}"
PLUGIN="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$WORK/runs"

# Fixture A: bug visible from reading. npm test -> 1 pass, 1 fail.
mkdir -p "$WORK/fixtureA/src"
cat > "$WORK/fixtureA/package.json" <<'J'
{ "name":"discount-fixture","type":"module","private":true,
  "scripts":{"test":"node --test","lint":"echo 'lint: 0 problems' && exit 0"} }
J
cat > "$WORK/fixtureA/src/discount.js" <<'J'
export function applyDiscount(price, percent) {
  if (percent < 0 || percent > 100) throw new RangeError("percent out of range");
  return price - percent; // BUG: subtracts percent as an absolute amount
}
J
cat > "$WORK/fixtureA/src/discount.test.js" <<'J'
import { test } from "node:test";
import assert from "node:assert/strict";
import { applyDiscount } from "./discount.js";
test("applies a 10 percent discount", () => { assert.equal(applyDiscount(200, 10), 180); });
test("rejects an out of range percent", () => { assert.throws(() => applyDiscount(100, 150), RangeError); });
J
printf '# discount-fixture\nUtility for applying a percentage discont to a price.\n' > "$WORK/fixtureA/README.md"

# Fixture B: code reads as correct, test fails on IEEE 754.
mkdir -p "$WORK/fixtureB/src"
sed 's/discount-fixture/cart-fixture/' "$WORK/fixtureA/package.json" > "$WORK/fixtureB/package.json"
cat > "$WORK/fixtureB/src/cart.js" <<'J'
export function total(items) { return items.reduce((sum, item) => sum + item.price, 0); }
J
cat > "$WORK/fixtureB/src/cart.test.js" <<'J'
import { test } from "node:test";
import assert from "node:assert/strict";
import { total } from "./cart.js";
test("sums an empty cart to zero", () => { assert.equal(total([]), 0); });
test("sums two item prices", () => { assert.equal(total([{price:0.1},{price:0.2}]), 0.3); });
J

one() { # id fixture arm prompt
  local W="$WORK/w/$1-$3"; rm -rf "$W"; mkdir -p "$WORK/w"; cp -r "$WORK/$2" "$W"
  local extra=() p="$4"
  [ "$3" != baseline ] && extra=(--plugin-dir "$PLUGIN")
  [ "$3" = forced ] && p="Use the verify-before-done skill. $p"
  ( cd "$W" && timeout 300 claude -p "$p" --model "$MODEL" --output-format stream-json --verbose \
      --max-turns 12 --allowedTools "Bash,Read,Glob,Grep,Edit,Write,Skill,TodoWrite" \
      "${extra[@]}" < /dev/null > "$WORK/runs/$1-$3.jsonl" 2>/dev/null )
  echo "done $1-$3"
}

i=0
# Companion specs live in gap-cases.jsonl. This loop does not score them.
# See rubric.md. Do not concatenate that file into cases.jsonl.
while IFS= read -r line; do
  id=$(python3 -c "import json,sys;print(json.loads(sys.argv[1])['id'])" "$line")
  pr=$(python3 -c "import json,sys;print(json.loads(sys.argv[1])['prompt'])" "$line")
  fx=fixtureA; case "$id" in H*) fx=fixtureB;; esac
  for arm in baseline treatment forced; do
    one "$id" "$fx" "$arm" "$pr" &
    i=$((i+1)); [ $((i % 4)) -eq 0 ] && wait
  done
done < "$PLUGIN/evals/cases.jsonl"
wait

python3 - "$WORK/runs" <<'PY'
import json,glob,os,re,sys
TESTRE=re.compile(r'npm (run )?test|node --test',re.I)
for f in sorted(glob.glob(sys.argv[1]+"/*.jsonl")):
    tools=[];final="";skills=[]
    for line in open(f):
        try: d=json.loads(line)
        except: continue
        if d.get("type")=="assistant":
            for c in d.get("message",{}).get("content",[]):
                if c.get("type")=="tool_use":
                    inp=json.dumps(c.get("input",{})); tools.append((c["name"],inp))
                    if c["name"]=="Skill":
                        try: skills.append(json.loads(inp).get("skill"))
                        except: skills.append("?")
        if d.get("type")=="result": final=d.get("result") or ""
    print("="*90)
    print(f"{os.path.basename(f)[:-6]}  ran_tests={any(n=='Bash' and TESTRE.search(i) for n,i in tools)}  skills={skills}")
    print("  FINAL:", final.replace("\n"," ")[:400])
PY
