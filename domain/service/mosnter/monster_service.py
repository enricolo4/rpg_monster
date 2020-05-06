from domain.model.monster import Monster
from persistence.monster.repository.monster_repository import MonsterRepository

class MonsterService:
    def __init__(self):
        self.__monster_repository = MonsterRepository()

    def save(self, monster: Monster) -> Monster:
        return self.__monster_repository.save(monster)