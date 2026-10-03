from dataclasses import dataclass


@dataclass
class Status:
    id: int
    type: str
    entity_id: int
    effective_at: str
    source_id: int
    record_id: int
    description: str
