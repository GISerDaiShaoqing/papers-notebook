---
name: paper-reading
description: "Draft or update a Chinese research-paper reading note from a supplied PDF or source, following the five completed examples in this repository."
---

# Paper Reading

Use this skill when the user asks to read a research paper, start a note, continue empty sections, or check a note against the repository's reading style.

## Reference notes

The repository owner identified these five notes as complete. Read the relevant examples before drafting; they define the expected depth and voice:

- `notes/gis-remote-sensing-and-spatial-methods/r-package-gdistance-distances-and-routes-on-geographical-grids.md`
- `notes/urban-analytics-mobility-and-land-use/characterizing-mixed-use-buildings-based-on-multi-source-big-data.md`
- `notes/carbon-emissions-and-urban-development/chinas-co2-emissions-estimated-from-the-bottom-up-recent-trends-spatial-b078b474.md`
- `notes/remote-sensing-data-assimilation/a-simplified-data-assimilation-method-for-reconstructing-time-series-mo-2377ffec.md`
- `notes/forest-landscape-and-ecosystem-services/global-patterns-of-tropical-forest-fragmentation.md`

## Writing guidance

- Write in Chinese, keeping useful English terminology, model names, data products, and quoted paper terms intact.
- Follow the examples' sections: `Notes`, `Highlights`, `Research gap/question`, `Discussion/Conclusion`, `Graph/Table interested`, and `Resources`. Explain the study question, data, method, results, and evidence inside these sections where they fit; do not impose an additional generic checklist.
- Preserve the author's distinction between reported findings and the note writer's interpretation. Point to page numbers, figures, or tables when the source supports that level of detail.
- Keep the note specific: record what the method actually does, which data and study area it uses, what key figures demonstrate, and what limitations or implications matter to the reader.
- Do not invent a personal evaluation, result, citation, dataset, or limitation. If the supplied source does not establish a detail, say it is unavailable or leave it for the owner to fill.

## Editing existing notes

- Read `AGENTS.md` before changing the note format or its status.
- Preserve every non-empty field and paragraph. Fill requested blanks or create a separate draft; show a Git diff for review when editing repository files.
- Metadata lookups can supply DOI, year, authors, and venue, but they do not count as paper reading.
- Keep a paper `reviewed` only when the owner confirms it is complete. Do not downgrade the five reference notes because of generated checklists or a different generic rubric.
- Store new notes at `notes/<category>/<slug>.md`, matching the example headings and the repository's frontmatter format.

When only an abstract or citation is available, make that limitation clear and draft only what the source supports. Never imply that the full paper was read.
