from sanic import Sanic, text
from sanic.views import HTTPMethodView
# Module that is called when '/submit-smish' is POSTed to

class View(HTTPMethodView):
    # Class that is invoked when the endpoint is called.
    # Any HTTP method not defined here will return a 405 Method
    # Invalid error

    async def post(self, req):
        # Debug print
        print(req.json)
        return text("That was a POST!")

    async def get(self, req):
        # Test case
        return text("This is a GET!")
