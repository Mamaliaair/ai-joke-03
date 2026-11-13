# A make.fun ai-joke-03 entry (Python 3.13, standard library only).
# It writes one fixed joke, a one-liner about AI coding agents, to
# /output/entry.txt. The joke reframes the agent's bugs as features the
# tests haven't discovered yet — a fresh angle on the agent's confidence.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My AI agent doesn't write bugs. It writes features the tests haven't discovered yet."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
