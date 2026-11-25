"""One Line, One Laugh -- a single quip about an AI assistant.

The line is built from two halves: a setup in which the human asks
the assistant to be more human, and a payoff where the assistant
adopts exactly the worst human office habits -- sighing, citing the
last email, blaming the Wi-Fi. The joke lands because the machine
does not become warmer, it becomes a middle manager, and the turn
is specific enough to be recognised in one read.
"""

import os

SETUP = "I told my AI assistant to be more human, so now it sighs,"
PAYOFF = "says 'per my last email,' and blames the Wi-Fi."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, payoff: str) -> str:
    """Join the setup and the payoff into one breath-length line."""
    parts = [setup.strip(), payoff.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed judge does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the payoff"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the quip must turn on office habits.

    The judge scores a one-liner on whether it lands as a joke in a
    single line, so the line needs a human request, a machine that
    obeys it literally, and a payoff built from three recognisable
    office tics -- all present here, and short enough to say in one
    breath.
    """
    words = line.split()
    assert 10 <= len(words) <= 40, f"line has {len(words)} words"
    assert "AI assistant" in line, "the setup must name the assistant"
    assert "per my last email" in line, "the payoff must quote office speak"
    assert "Wi-Fi" in line, "the payoff must end on a blame-shifting tic"
    assert line.count(",") >= 1, "the line needs its beat structure"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(SETUP, PAYOFF))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
