# ankh

A CLI flashcard tool with spaced repetition, written in Python.

> **Status:** early work in progress — core functionality is still being built out.

## Planned features

- Create and manage flashcard decks from the command line
- Simple pass/fail spaced repetition scheduling
- Local JSON storage — no server, no account needed

## Installation

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/lenhard01/ankh.git
cd ankh
uv sync
```

## Development

```bash
uv run ruff check .
uv run ruff format .
uv run ty check .
```

## License

MIT — see [LICENSE](./LICENSE).
