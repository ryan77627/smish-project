import pickle

class campaignDB:
    def __init__(self):
        with open('phish_db/phish_campaigns.db', 'rb+') as e:
            try:
                self.__db = pickle.load(e)
            except FileNotFoundError:
                self.__db = {}

    def __del__(self):
        with open('phish_db/phish_campaigns.db', 'wb+') as e:
            pickle.dump(self.__db, e)

    def getCampaigns(self):
        return self.__db

    def addCampaign(self, campaignID):
        if campaignID not in self.__db:
            self.__db[campaignID] = []
        else:
            pass # We already have it, no need to worry

    def addEndpointID(self, campaignID, endpointID):
        if campaignID in self.__db:
            self.__db[campaignID].append("endpointID")
        else:
            raise ValueError("Campaign ID not initialized.")

class phishDB:
    def __init__(self, campaign_id):
        with open(f'phish_db/{campaign_id}.db', 'rb+') as e:
            try:
                self.__db = pickle.load(e)
            except FileNotFoundError:
                self.__db = {}

    def getCampaignDetails(self):
        return self.__db

    def addEndpoint(self, uid, endpoint):
        self.__db[endpoint] = uid
