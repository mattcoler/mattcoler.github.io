# Runs before every build (see pre-render in _quarto.yml).
# Stops the build if a publication lacks a type or a topic.
import re, sys
TYPES = {"Journal article", "Conference paper", "Book chapter", "Book", "Preprint", "Report", "Patent", "Dataset"}
text = open("publications.yml", encoding="utf-8").read()
problems = []
for block in re.split(r"\n- title: ", "\n" + text)[1:]:
    title = block.split("\n", 1)[0].strip().strip('"')
    m = re.search(r"categories:\s*\[(.*?)\]", block)
    cats = [c.strip() for c in m.group(1).split(",")] if m else []
    n_types = sum(c in TYPES for c in cats)
    n_topics = sum(c not in TYPES for c in cats)
    if n_types != 1 or n_topics < 1:
        problems.append(f"  - {title[:70]}  {cats}")
if problems:
    print("publications.yml: each entry needs exactly one type and at least one topic:")
    print("\n".join(problems))
    sys.exit(1)
