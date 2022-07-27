######################

# Smishing Server entrypoint

######################
import sys
sys.path.append('../')
from sanic import Sanic
import backend.submitSmish as submitSmish
import backend.userStore as userStore
import backend.api as api
import backend.login_handler as login_handler

# Initialize any users in the DB
us = userStore.UserStore()

def main():

    app = Sanic("endpoint-listener")


    # Submit phish route
    app.add_route(submitSmish.View.as_view(), '/submit-smish')

    # Submit frontend gen user tree route
    app.add_route(api.genTree.as_view(), '/api/genTree')

    # Route to mark a successful smish
    #@app.get("/login/<id>")
    #async def handler(req, id):
    #    login_handler.recordClick(req, id)

    app.add_route(login_handler.recordClick.as_view(), '/login/<id>')
    
    # We are ready, deploy!
    app.run(host='0.0.0.0', port=1234, access_log=False, workers=2)

    us = None

if __name__ == "__main__":
    main()
