from dataclasses import dataclass


@dataclass
class Event:
    id: int
    type: str
    title: str
    occurred_at: str
    location: str
    description: str
