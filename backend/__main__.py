######################

# Smishing Server entrypoint

######################
import sys
sys.path.append('../')
from sanic import Sanic
import backend.submitSmish as submitSmish
import backend.userStore as userStore

def main():

    app = Sanic("endpoint-listener")

    # Initialize any users in the DB
    userStore = userStore.UserStore()

    # Submit phish route
    app.add_route(submitSmish.View.as_view(), '/submit-smish')
    
    # We are ready, deploy!
    app.run(host='0.0.0.0', port=1234, access_log=False, workers=2)

if __name__ == "__main__":
    main()
