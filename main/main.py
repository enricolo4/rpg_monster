import falcon as falcon
from waitress import serve

from controller.health.health_controller import HealthController
from controller.monster.monster_controller import MonsterController

app = falcon.API()

app.add_route("/monster", MonsterController())
app.add_route("/health", HealthController())

