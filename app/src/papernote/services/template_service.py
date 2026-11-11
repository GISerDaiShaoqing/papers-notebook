from __future__ import annotations


NEW_NOTE_TEMPLATE = """---
title: "{title}"
category: "{category}"
status: unread
source: ""
---

# {title}

## Bibliographic information

- Link: 
- DOI: 

## Notes


## Highlights


## Research gap/question


## Discussion/Conclusion


## Graph/Table interested


## Resources


"""


LEGACY_TEMPLATE = """**Title:** {title}

**Link:** [原文链接]()

**Doi:** 

**Notes:** 

**Highlights:** 

**Research gap/question:** 

**Discussion/Conclusion:** 

**Graph/Table interested:** 

**Resources:** 
"""


def new_note_template(title: str, category: str) -> str:
    return NEW_NOTE_TEMPLATE.format(title=title.replace('"', '\\"'), category=category.replace('"', '\\"'))


def legacy_template(title: str) -> str:
    return LEGACY_TEMPLATE.format(title=title)

