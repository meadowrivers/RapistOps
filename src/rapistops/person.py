from dataclasses import dataclass


@dataclass
class Person:
    id: int
    name: str
    identifiers: str
    description: str
    created_at: str
    updated_at: str
