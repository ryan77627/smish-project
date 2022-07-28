from sanic import Sanic, response
from sanic.views import HTTPMethodView
import backend.dbConnectors as dbConnectors

class recordClick(HTTPMethodView):
    async def get(self, req, id):
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

class recordSubmit(HTTPMethodView):
    async def post(self, req):
        id = req.cookies.get('phid')

        # Determine which campaign this endpoint is for
        campaign_db = dbConnectors.campaignDB()
        campaign = campaign_db.findCampaign(id)
        campaign_db = None
        phish_db = dbConnectors.phishDB(campaign)
        phish_db.userPosted(id)

        return response.redirect("https://google.com")

