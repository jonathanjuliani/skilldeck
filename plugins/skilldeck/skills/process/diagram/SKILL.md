---
name: diagram
description: Choose the right diagram or visual for what is being explained and render it. Use when an explanation involves a flow, a sequence of interactions, a data model, a system's structure, a state machine, a schedule or phases, a hierarchy, or a comparison, and words alone would be harder to follow than a picture. Not for deciding a product's navigation and screen structure, which is information-architecture, and not for a point a single sentence already carries.
---

# Diagram

Pick the diagram that fits what you are trying to communicate, then render it. The choice of diagram type carries most of the value: the wrong type obscures more than prose would.

The defining constraint: the diagram type is chosen from the *shape of the idea*, not from habit. A sequence of interactions is never a flowchart; a data model is never a mind map. Match the visual to the structure, or do not draw one.

## Decide first

Before rendering, name what you are showing and map it to a type. The full mapping with examples is in [when-to-use.md](when-to-use.md). The short version:

- **Process or decision flow** (steps, branches): flowchart.
- **Interactions over time** (who calls whom, in what order): sequence diagram.
- **Data model** (entities and relationships): entity-relationship diagram.
- **System structure at a chosen zoom** (context, containers, components): C4 (rendered as a flowchart with C4 conventions).
- **Lifecycle or status machine** (states and transitions): state diagram.
- **Schedule or phased plan** (work over time): Gantt or a timeline.
- **Hierarchy or breakdown** (tree of parts): tree or mind map.
- **Comparison across options and dimensions**: a table or matrix, not a diagram.
- **Quantities**: a chart. For anything data-heavy or styled, hand it to a charting skill; Claude Code ships `dataviz` for this.

If two types seem to fit, you are probably trying to show two things: draw two diagrams, each doing one job, rather than one that does neither well.

## Then render

- **Default to Mermaid.** It renders inline in most surfaces, versions well in text, and covers flowchart, sequence, ERD, state, Gantt, class, and mind map. Produce a fenced `mermaid` block.
- **Keep it legible.** Aim for the fewest nodes that make the point. If a diagram exceeds roughly a dozen nodes, split it or zoom out a level. Label edges with what actually happens, not "yes/no" where a verb is clearer.
- **Reach for richer tools when Mermaid falls short.** For a polished or interactive visual, an SVG or an HTML widget is better; for quantitative charts use the dataviz skill; for a real architecture canvas the user will edit, offer a FigJam or Figma export if that toolchain is available. Say why you switched.
- **Validate before presenting.** Make sure the Mermaid parses (correct diagram header, matched brackets, no reserved-word node ids). A broken diagram is worse than a paragraph.

## Rules

- **Type before tool.** Decide what shape you are drawing before choosing how to render it.
- **One idea per diagram.** Split rather than overload.
- **Prose still wins sometimes.** Three sequential steps need a sentence, not a flowchart. Draw only when structure genuinely outpaces words.
- **Accompany, do not replace.** A diagram carries the structure; a line or two of text carries the takeaway. Give both.

## When this does not apply

Most explanations do not need a picture. Skip it for three sequential steps, for anything a sentence conveys, and where the structure is already visible in code the reader can open. A diagram that restates prose costs a context switch and returns nothing.

## Before you hand it over

Check the rendered output rather than the source you intended: it parses, it carries one idea, and its node count is small enough to read at a glance. A diagram that fails to render is worse than the paragraph it replaced.
