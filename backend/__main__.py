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

if __name__ == "__main__":
    main()
