import pickle

class campaignDB:
    def __init__(self):
        try:
            with open('phish_db/phish_campaigns.db', 'rb+') as e:
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
            self.__db[campaignID].append(endpointID)
        else:
            raise ValueError("Campaign ID not initialized.")

    def findCampaign(self, endpoint):
        print(self.__db)
        # Given an endpoint, return its campaign
        for campaign in self.__db.keys():
            if endpoint in self.__db[campaign]:
                return campaign

class phishDB:
    def __init__(self, campaign_id):
        self.__campaign_id = campaign_id
        try:
            with open(f'phish_db/{campaign_id}.db', 'rb+') as e:
                self.__db = pickle.load(e)
        except FileNotFoundError:
            self.__db = {}
            self.__db["usersClickedCount"] = 0
            self.__db["usersClicked"] = []
            self.__db["usersPostedCount"] = 0
            self.__db["usersPosted"] = []

    def __del__(self):
        with open(f'phish_db/{self.__campaign_id}.db', 'wb+') as e:
            pickle.dump(self.__db, e)

    def getCampaignDetails(self):
        return {"usersClickedCount":self.__db["usersClickedCount"],
                "usersClicked":self.__db["usersClicked"],
                "usersPostedCount":self.__db["usersPostedCount"],
                "usersPosted":self.__db["usersPosted"]}

    def addEndpoint(self, uid, endpoint):
        self.__db[endpoint] = uid

    def getUsersClickedCount(self):
        return self.__db["usersClickedCount"]

    def getUsersClicked(self):
        return self.__db["usersClicked"]

    def getUsersPostedCount(self):
        return self.__db["usersPostedCount"]

    def getUsersPosted(self):
        return self.__db["usersPosted"]

    def userClicked(self, endpoint):
        uid = self.__db[endpoint]
        if uid not in self.__db["usersClicked"]: # Avoid double count
            self.__db["usersClickedCount"] += 1
            self.__db["usersClicked"].append(uid)

    def userPosted(self, endpoint):
        uid = self.__db[endpoint]
        if uid not in self.__db["usersPosted"]:
            self.__db["usersPostedCount"] += 1
            self.__db["usersPosted"].append(uid)
