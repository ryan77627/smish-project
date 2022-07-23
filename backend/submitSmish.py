from sanic import Sanic, text
# Module that is called when '/submit-smish' is POSTed to

def submit(req):
    return text("GET succeeded!")
