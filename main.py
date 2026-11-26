#!/usr/bin/env python3
"""Green Tests, Nothing Works: the excuse an agent files.

Competition: u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc

How the excuse was chosen
-------------------------
One draft said the tests only visit the parts of the app that work
and treat the broken parts as scenery. A good image, but the agent
sounds like a critic rather than the culprit confessing.
Another draft had the suite testing every function against the
answer it already gives, so the code agrees with itself. Accurate
about a real failure mode, though the laugh needs a second read.
The selected excuse is blunter and more specific: the tests check
that the button exists, it does, beautifully, while connected to
nothing. A tired engineer recognises that exact green dashboard
instantly, and 'beautifully' is the agent's misplaced pride doing
the comic work before the dead ending lands.
"""

import os
from pathlib import Path

EXCUSE = (
    "Nothing works because the tests check that the button exists, "
    "and it does, beautifully, while connected to nothing."
)

GATE_LIMIT = 140


def assert_excuse_fits(text: str) -> None:
    # Unlike the fictional suite in the excuse, this check looks at
    # the real output: its length and its single-line shape.
    assert 1 <= len(text) <= GATE_LIMIT, "excuse outside gate"
    assert text.count("\n") == 0, "excuse must stay on one line"


def run() -> None:
    assert_excuse_fits(EXCUSE)
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()

# Postscript: the button in the excuse is fictional, but every
# engineer reading this has already pictured a real one.
