from dataclasses import dataclass


@dataclass
class Institution:
    id: int
    name: str
    type: str
    jurisdiction: str
    location: str
    description: str
    created_at: str
    updated_at: str
