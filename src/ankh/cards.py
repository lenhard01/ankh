import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

ANKH_FILE = Path("ankh.json")


@dataclass
class Card:
    front: str
    back: str
    last_reviewed: date | None = None
    review_count: int = 0
    interval_days: int = 1


def load_cards() -> list[Card]:
    if not ANKH_FILE.exists():
        return []
    with ANKH_FILE.open() as filepath:
        data = json.load(filepath)
    return [
        Card(
            front=d["front"],
            back=d["back"],
            last_reviewed=date.fromisoformat(d["last_reviewed"])
            if d["last_reviewed"]
            else None,
            review_count=d["review_count"],
            interval_days=d["interval_days"],
        )
        for d in data
    ]


def save_cards(cards: list[Card]) -> None:
    with ANKH_FILE.open("w") as filepath:
        json.dump(
            [
                {
                    **asdict(card),
                    "last_reviewed": card.last_reviewed.isoformat()
                    if card.last_reviewed
                    else None,
                }
                for card in cards
            ],
            filepath,
            indent=2,
        )
