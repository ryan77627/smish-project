# This will be responsible for generating the route for a user's smish url and storing it where we can grab it later
# Example: '/login-najhf'

import pickle
import random
import string

def gen_url():
    phish_db = open_db(campaign_id) # Returns an empty/populated dictionary
    # This will eventually take a user as a parameter
    uid = 1
    rand_string = random.choices(string.ascii_letters, k=5)
    phish_db[rand_string] = uid

    ret_url = '/login-' + rand_string

    # Pickle the DB and store file
    save_db(campaign_id, phish_db)

    return ret_url

def open_db(phish_campaign):
    # Unpickle and open the database for writing
    with open(f'phish_db/{phish_campaign}.db', 'w') as f:
        try:
            phish_db = pickle.load(f)
        except io.UnsupportedOperation:
            # File doesn't exist, create a new campaign db and track it
            phish_db = dict()

    with open('phish_campaigns.db', 'w') as e:
        try:
            db = pickle.load(e)
        except io.UnsupportedOperation:
            db = []
        db.append(phish_campaign)
        db = pickle.dump(db, e)


    return phish_db

def close_db(phish_campaign, phish_db):
    with open(f'phish_db/{phish_campaign}.db', 'w') as f:
        pickle.dump(phish_db, f)
