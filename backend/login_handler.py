from sanic import Sanic, response
from sanic.views import HTTPMethodView
import backend.dbConnectors as dbConnectors

class recordClick(HTTPMethodView):
    async def get(self, req, id):
        # Detect if iMessage preview
        if req.headers.get("User-Agent").lower() == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0".lower(): # Convert to lower just in case there are variations in the string
            # iMessage preview! Don't count as get and send meta tags >:)
            return response.html('<html><head><meta property="og:title" content="You have been logged out your account. Please log back in to regain access." /><meta property="og:image" content="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2MVHB5XTud6Yf1SojaEuDxMS8u6_ByXDxiA&usqp=CAU" /><title>Login</title></head><body></body></html>')

        # We should only get here for an actual GET request
        print(f"GET for endpoint: {id}")
        resp = response.redirect('/login')
        resp.cookies['phid'] = id

        # Determine which campaign this endpoint is for
        campaign_db = dbConnectors.campaignDB()
        campaign = campaign_db.findCampaign(id)
        print(f"Loading campaign DB for {campaign}")
        campaign_db = None
        phish_db = dbConnectors.phishDB(campaign)
        phish_db.userClicked(id)

        return resp

    # Record a POST action on the login form. Uses same endpoint.
    async def post(self, req, id):
        id = req.cookies.get('phid')

        # Determine which campaign this endpoint is for
        campaign_db = dbConnectors.campaignDB()
        campaign = campaign_db.findCampaign(id)
        campaign_db = None
        phish_db = dbConnectors.phishDB(campaign)
        phish_db.userPosted(id)

        return response.redirect("https://google.com")

