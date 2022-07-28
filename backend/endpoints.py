# This will be responsible for generating the route for a user's smish url and storing it where we can grab it later
# Example: '/login/najhf'

import pickle
import random
import string
import io
import backend.dbConnectors as dbConnectors

# TODO: Refactor DB code out of this module

def gen_url(uid):
    campaign_id = 'test-id'
    phishcampaign_db = dbConnectors.campaignDB()
    # Ensure our campaign exists
    phishcampaign_db.addCampaign(campaign_id)
    rand_string = ''.join(random.choices(string.ascii_letters, k=5))
    phish_db = dbConnectors.phishDB()
    phish_db.add_endpoint(uid, randstring)
    phishcampaign_db.addEndpointID(campaign_id, rand_string)

    ret_url = '/login/' + rand_string

    # Pickle the DB and store file (by dereferencing)
    phishcampaign_db = None
    phish_db = None

    return ret_url

"""
def open_db(phish_campaign):
    # Unpickle and open the database for writing
    try:
        with open(f'phish_db/{phish_campaign}.db', 'rb+') as f:
            phish_db = pickle.load(f)
    except FileNotFoundError:
        # File doesn't exist, create a new campaign db and track it
        phish_db = dict()
    
    try:
        with open('phish_db/phish_campaigns.db', 'rb+') as e:
            db = pickle.load(e)
    except FileNotFoundError:
        db = {}
    if phish_campaign not in db:
        db[phish_campaign] = []
        with open('phish_db/phish_campaigns.db', 'wb+') as e:
            db = pickle.dump(db, e)


    return phish_db

def save_db(phish_campaign, phish_db):
    with open(f'phish_db/{phish_campaign}.db', 'wb+') as f:
        pickle.dump(phish_db, f)
"""
