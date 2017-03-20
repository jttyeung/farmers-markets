from server import *
from model import *


def get_market_ids():
    """ Gets full list of farmer's market ids. """
    fm_ids = set([])

    market_ids = db.session.query(FarmersMarket.fm_id).all()
    for ids in market_ids:
        fm_ids.add(ids[0])

    return fm_ids


def get_markets():
    """ Gets full list of farmer's markets. """

    markets = { 'markets': [] }

    # QUERY = """
    #     SELECT row_to_json(farmersmarkets)
    #     FROM farmersmarkets
    #     """

    # db_cursor = db.session.execute(QUERY)
    # rows = db_cursor.fetchall()

    # for row in rows:
    #     print row
    #     markets['markets'].append(row)

    db_markets = db.session.query(FarmersMarket).all()
    hell0 = db_markets[0].__dict__
    del hell0['_sa_instance_state']
    print hell0


    for market in db_markets:
        markets['markets'].append(market.__dict__)
        del market['_sa_instance_state']

    # markets['markets'].append(db_markets[0].__dict__)

    return markets



# how to store the data? in database format, view with json format?
