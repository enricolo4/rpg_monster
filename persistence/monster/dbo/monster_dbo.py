import uuid
from uuid import UUID
from dataclasses import dataclass

from domain.model.monster import Monster


@dataclass
class MonsterDBO:
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
    id: UUID

    def to_model(self) -> Monster:
        return Monster(
            id=self.id,
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


def monster_to_dbo(monster: Monster) -> MonsterDBO:
    return MonsterDBO(
        id=uuid.uuid4(),
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
