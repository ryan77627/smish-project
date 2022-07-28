from sanic import Sanic, text
from sanic.views import HTTPMethodView
from backend.twilio import send as twilio
from backend import endpoints
import backend.__main__ as config
import json
# Module that is called when '/submit-smish' is POSTed to

BASE_DOMAIN = "https://theinfoseccorner.com"

class View(HTTPMethodView):
    # Class that is invoked when the endpoint is called.
    # Any HTTP method not defined here will return a 405 Method
    # Invalid error

    async def post(self, req):
        req = req.json
        # Parse the message to be the message with the URL
        msg = req['msg'].format(URL = BASE_DOMAIN + endpoints.gen_url(req['uid']))
        try:
            twilio.Send(config.us.get_user(req['uid']).phonenum, msg)
            return text("Successful!")
            #return text(msg)
        except Exception as e:
            print(e)
            return text("SMS send failure!")

