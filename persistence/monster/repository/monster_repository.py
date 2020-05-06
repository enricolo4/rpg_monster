from domain.model.monster import Monster
from persistence.monster.dbo.monster_dbo import MonsterDBO, monster_to_dbo


class MonsterRepository:
    def save(self, monster: Monster) -> Monster:
        monster_converted_to_dbo: MonsterDBO = monster_to_dbo(monster)
        monster_dbo = self.__save_sql_alchemy(monster_converted_to_dbo)

        return monster_dbo.to_model()

    def __save_sql_alchemy(self, monster_dbo: MonsterDBO) -> MonsterDBO:
        return monster_dbo
