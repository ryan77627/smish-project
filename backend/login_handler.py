from sanic import Sanic, response
from sanic.views import HTTPMethodView

class recordClick(HTTPMethodView):
    async def get(self, req, id):
        print(f"GET for endpoint: {id}")
        resp = response.redirect('/login')
        resp.cookies['phid'] = id
        return resp

