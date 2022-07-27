from sanic import Sanic, response
from sanic.views import HTTPMethodView
import backend.__main__ as config
import json

BASE_DOMAIN = "https://theinfoseccorner.com"

class genTree(HTTPMethodView):
    # Class that is invoked when the endpoint is called.
    # Any HTTP method not defined here will return a 405 Method
    # Invalid error
    
    async def get(self, req):
        print(f"{req.args}")
        us = config.us
        # We should get a dict that is {"name":["item"]}
        user_name = req.args["user"][0]
        user = us.lookup_user(user_name)

        return response.json(self.__create_json(user))

    def __create_json(self, user,depth=1):
        if not user.employees:
            if depth == 1:
                return {'name': user.name, 'employees': []}
            return []
        else:
            emp = []
            for e in user.employees:
                emp.append({'name':e.name, 'employees':self.__create_json(e,depth+1)})

            if depth == 1:
                return {'name':user.name, "employees": emp}
            else:
                return emp
