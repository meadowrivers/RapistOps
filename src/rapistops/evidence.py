from dataclasses import dataclass


@dataclass
class Evidence:
    id: int
    type: str
    source_id: int
    provenance_id: int
    record_id: int
    reference: str
    description: str
