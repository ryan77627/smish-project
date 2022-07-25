from sanic import Sanic, text
from sanic.views import HTTPMethodView
from backend.twilio import main as twilio
from backend.twilio.creds import SenderNumber
import json
# Module that is called when '/submit-smish' is POSTed to

class View(HTTPMethodView):
    # Class that is invoked when the endpoint is called.
    # Any HTTP method not defined here will return a 405 Method
    # Invalid error

    async def post(self, req):
        # Debug print
        req = req.json
        print(req)
        try:
            twilio.send_sms(req["msg"], SenderNumber, req['to'])
            return text("Successful!")
        except Exception as e:
            print(e)
            return text("SMS send failure!")

    async def get(self, req):
        # Test case
        return text("This is a GET!")
