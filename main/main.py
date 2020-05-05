import falcon as falcon
from falcon import Response, Request, json

application = falcon.API()


class HealthController:
    def on_get(self, request: Request, response: Response):
        response.body = json.dumps({"status": "up"})


application.add_route("/health", HealthController())
