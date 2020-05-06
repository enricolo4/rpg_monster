from falcon import Request, Response, json

from controller.monster.dto.monster_dto import MonsterDTO
from domain.model.monster import Monster
from domain.service.mosnter.monster_service import MonsterService


class MonsterController:
    def __init__(self):
        self.__monster_service = MonsterService()

    def on_post(self, request: Request, response: Response):
        monster_dto = MonsterDTO(**request.media)

        monster: Monster = self.__monster_service.save(monster_dto.to_model)

        response.body = json.dumps(monster_dto(monster).__dict__)

