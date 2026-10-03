from dataclasses import dataclass


@dataclass
class Case:
    id: int
    type: str
    name: str
    identifier: str
    description: str
    opened_at: str
    closed_at: str
