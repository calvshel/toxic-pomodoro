#!/usr/bin/env python3
"""A standard-library Pomodoro timer with a deeply unhelpful exit strategy."""

from __future__ import annotations

import random
import sys
import time

WORK_SECONDS = 25 * 60
ROASTS = [
    "You surrendered to a clock. Tragic, but on-brand.",
    "That was not burnout. That was your attention span filing a resignation letter.",
    "You lasted less than a Pomodoro. The dopamine lobby sends its regards.",
    "Your focus broke first and your ego is already trying to spin the narrative.",
    "One timer and you folded. That's not multitasking, that's surrender cosplay.",
    "You could not even sit still for 25 minutes. Embarrassing, yet educational.",
    "The tomato won. You are currently being outworked by kitchen decor.",
    "This interruption was brought to you by the very same impulse that ruined your last five tabs.",
    "Focus was available for a limited time only and you left it on read.",
    "You did not quit the timer. You negotiated with your own attention and lost.",
]


def format_time(seconds: int) -> str:
    minutes, remainder = divmod(max(seconds, 0), 60)
    return f"{minutes:02d}:{remainder:02d}"


def render_line(message: str) -> None:
    sys.stdout.write("\r\x1b[2K" + message)
    sys.stdout.flush()


def run_timer(duration: int = WORK_SECONDS) -> None:
    end_time = time.monotonic() + duration
    try:
        while True:
            remaining = int(round(end_time - time.monotonic()))
            if remaining <= 0:
                render_line("25:00 complete. Go touch grass.\n")
                return
            render_line(f"Pomodoro active | time remaining: {format_time(remaining)}")
            time.sleep(1)
    except KeyboardInterrupt:
        roast = random.choice(ROASTS)
        sys.stdout.write("\n\x1b[31;1m" + roast + "\x1b[0m\n")
        sys.stdout.flush()


def main() -> None:
    run_timer()


if __name__ == "__main__":
    main()
