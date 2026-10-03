from dataclasses import dataclass


@dataclass
class Relationship:
    id: int
    source_entity_id: int
    target_entity_id: int
    type: str
    source_id: int
    record_id: int
    effective_at: str
    description: str
