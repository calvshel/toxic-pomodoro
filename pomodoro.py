#!/usr/bin/env python3
"""A standard-library Pomodoro timer with a deeply unhelpful exit strategy."""

from __future__ import annotations

import random
import sys
import time
from argparse import ArgumentParser

WORK_SECONDS = 25 * 60
BREAK_SECONDS = 5 * 60
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


def parse_args(argv: list[str] | None = None):
    parser = ArgumentParser(description="Run a Pomodoro timer that roasts you if you quit early.")
    parser.add_argument("--minutes", type=float, default=25, help="work duration in minutes (default: 25)")
    parser.add_argument("--break", dest="break_mode", action="store_true", help="run a 5-minute break timer instead")
    parser.add_argument("--calm", action="store_true", help="exit quietly on Ctrl+C")
    parser.add_argument("--seed", type=int, default=None, help="seed roast selection for repeatable demos")
    return parser.parse_args(argv)


def duration_from_args(args) -> int:
    if args.break_mode:
        return BREAK_SECONDS
    seconds = int(round(args.minutes * 60))
    if seconds <= 0:
        raise ValueError("--minutes must be greater than 0")
    return seconds


def format_time(seconds: int) -> str:
    minutes, remainder = divmod(max(seconds, 0), 60)
    return f"{minutes:02d}:{remainder:02d}"


def render_line(message: str) -> None:
    sys.stdout.write("\r\x1b[2K" + message)
    sys.stdout.flush()


def run_timer(duration: int = WORK_SECONDS, calm: bool = False, rng: random.Random | None = None) -> None:
    end_time = time.monotonic() + duration
    rng = rng or random.Random()
    try:
        while True:
            remaining = int(round(end_time - time.monotonic()))
            if remaining <= 0:
                render_line("25:00 complete. Go touch grass.\n")
                return
            render_line(f"Pomodoro active | time remaining: {format_time(remaining)}")
            time.sleep(1)
    except KeyboardInterrupt:
        if calm:
            sys.stdout.write("\nTimer stopped.\n")
            sys.stdout.flush()
            return
        roast = rng.choice(ROASTS)
        sys.stdout.write("\n\x1b[31;1m" + roast + "\x1b[0m\n")
        sys.stdout.flush()


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    try:
        duration = duration_from_args(args)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    run_timer(duration=duration, calm=args.calm, rng=random.Random(args.seed))


if __name__ == "__main__":
    main()
