# Installing a block into a repo's agent instructions

How `setup-skills` adds one of this pack's blocks to a repository's agent instructions file. Two blocks use this procedure, and it is identical for both. The text to install is the whole of the payload file, markers included, and nothing from this file.

| Block | Payload | Marker |
| --- | --- | --- |
| Verification | [verification-block.md](verification-block.md) | `skilldeck-skills:verification` |
| Routing | [routing-block.md](routing-block.md) | `skilldeck-skills:routing` |

Both exist for the same reason. The skills they stand in for are model-invoked, and a completion gate is needed at the moment a claim is written, while a routing hint is needed at the moment a task starts. Neither can wait to be reached for. A repo's agent instructions file is read every turn without an invocation, so a short version lives there and the skill stays as the detail behind it.

Each block is offered separately and installed only on its own yes. They are independent: a repo may carry either, both, or neither.

## The one thing that must not go wrong

**You are adding to a file someone else owns.** Every heading, rule, and line already in that file must still be there when you are done. This step has exactly one destructive failure mode, which is rewriting the file instead of adding to it, so:

- **Read the target file in full before writing anything.**
- **Use a surgical edit.** Never write the file wholesale, and never reconstruct it from memory. If your tool for this is a whole-file write, read the current contents, and write them back with the block added.
- **After writing, confirm every heading that was there before is still there.** If anything is missing, restore it before reporting.

## Steps

1. **Pick the file.** `AGENTS.md` if it exists, otherwise `CLAUDE.md`. If both exist, ask which one the team treats as canonical. If neither exists, offer `AGENTS.md`, since it is the cross-tool convention and this plugin does not assume a vendor. Creating a file is the only case where there is no prior content to preserve.
2. **Look for the markers.** Search the target for the block's own `:begin` marker from the table above.
   - **Absent**: append the block at the end of the file, unless the file has an obvious conventions or workflow section it belongs in.
   - **Present, and the text between the markers matches the payload file**: change nothing. Say it is already installed and stop. This is the normal outcome of a repeat run.
   - **Present, and the text differs**: someone has edited it, or the block has been updated in this pack. Show the difference and ask before replacing. Replace only what lies between the markers.
3. **Never write a second copy.** One pair of markers per block per file, always. A file carrying both blocks has two pairs, and neither may be nested inside the other.
