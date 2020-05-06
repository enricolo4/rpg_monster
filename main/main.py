import falcon as falcon
from waitress import serve

from controller.health.health_controller import HealthController
from controller.monster.monster_controller import MonsterController

app = falcon.API()

app.add_route("/monster", MonsterController())
app.add_route("/health", HealthController())

if __name__ == '__main__':
    serve(app=app, host="127.0.0.1", port=5555)