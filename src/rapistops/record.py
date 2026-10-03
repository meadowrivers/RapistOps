from dataclasses import dataclass


@dataclass
class Record:
    id: int
    source_id: int
    provenance_id: int
    type: str
    title: str
    source_reference: str
    created_at: str
    published_at: str
    collected_at: str
