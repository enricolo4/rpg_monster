from dataclasses import dataclass
from uuid import UUID
from typing import Optional

@dataclass
class Monster:
    race: str
    armor_class: str
    speed: UUID
    life: UUID
    strength: UUID
    dexterity: UUID
    intelligence: UUID
    charisma: UUID
    wisdom: UUID
    constitution: UUID
    id: Optional[UUID] = None
