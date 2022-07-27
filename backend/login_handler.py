from sanic import Sanic, response
from sanic.views import HTTPMethodView

class recordClick(HTTPMethodView):
    async def get(self, req, id):
        print(f"{id}")

