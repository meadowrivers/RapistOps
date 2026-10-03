from dataclasses import dataclass


@dataclass
class Source:
    id: int
    name: str
    type: str
    organization: str
    location: str
    access_reference: str
