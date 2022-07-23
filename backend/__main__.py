######################

# Smishing Server entrypoint

######################
from sanic import Sanic
import backend.submitSmish as submitSmish

def main():

    app = Sanic("endpoint-listener")

    @app.route('/submit-smish')
    async def handler(request):
        return submitSmish.submit(request) # There may be better ways to do this, may refactor later on with actual classes?

    
    # We are ready, deploy!
    app.run(host='0.0.0.0', port=1234, access_log=False, workers=2)

if __name__ == "__main__":
    main()
