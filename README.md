# Toxic Pomodoro

A dependency-free terminal Pomodoro timer that keeps the countdown calm until you try to quit early. Then it gets personal.

Toxic Pomodoro is a tiny Python CLI for focused 25-minute work sprints. It updates on a single terminal line, catches `Ctrl+C`, and exits with a randomly selected red roast for anyone who negotiates with their own attention span.

## Features

- Standard 25-minute Pomodoro countdown
- Single-line dynamic terminal display
- Pure Python standard library, no packages required
- Graceful `KeyboardInterrupt` handling
- Ten hardcoded sarcastic anti-quit messages
- ANSI red formatting for dramatic early exits
- Custom work duration with `--minutes`
- Break timer mode with `--break`
- Calm interrupt mode with `--calm`
- Unit tests for duration parsing and formatting

## Quick Start

```bash
python3 pomodoro.py
```

The timer starts immediately:

```text
Pomodoro active | time remaining: 24:59
```

Pressing `Ctrl+C` before completion prints one random roast and exits.

## Options

```bash
python3 pomodoro.py --minutes 45
python3 pomodoro.py --break
python3 pomodoro.py --calm
python3 pomodoro.py --seed 7
```

## Why This Exists

Most focus timers try to be gentle. Toxic Pomodoro is for people who respond better to theatrical accountability. It is intentionally small, inspectable, and easy to modify.

## Requirements

- Python 3.8 or newer
- A terminal with ANSI colour support for the red roast output

## Development

There is no packaging or build system. The whole app lives in one file:

```text
pomodoro.py
```

Run a syntax check with:

```bash
python3 -m py_compile pomodoro.py
python3 -m unittest -v
```

## Roadmap

- Session completion log
- Configurable roast intensity
- Optional sound on completion

## License

MIT License

Copyright (c) 2026 Calvin Shelwell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
