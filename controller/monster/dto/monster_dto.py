import uuid
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from domain.model.monster import Monster


@dataclass
class MonsterDTO:
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
    id: Optional[str] = None

    @property
    def to_model(self) -> Monster:
        return Monster(
            race=self.race,
            armor_class=self.armor_class,
            speed=self.speed,
            life=self.life,
            strength=self.strength,
            dexterity=self.dexterity,
            intelligence=self.intelligence,
            charisma=self.charisma,
            wisdom=self.wisdom,
            constitution=self.constitution
        )

def monster_to_dto(monster: Monster) -> MonsterDTO:
    return MonsterDTO(
        id=str(monster.id),
        race=monster.race,
        armor_class=monster.armor_class,
        speed=monster.speed,
        life=monster.life,
        strength=monster.strength,
        dexterity=monster.dexterity,
        intelligence=monster.intelligence,
        charisma=monster.charisma,
        wisdom=monster.wisdom,
        constitution=monster.constitution
    )