from server import *
from model import *


def get_market_ids():
    """ Gets full list of farmer's market ids. """
    fm_ids = set([])

    market_ids = db.session.query(FarmersMarket.fm_id).all()
    for ids in market_ids:
        fm_ids.add(ids[0])
    print fm_ids
    return fm_ids


def get_markets():
    """ Gets full list of farmer's markets. """

    markets = { 'markets': [] }

    # Converts each row to a dictionary
    QUERY = """
        SELECT row_to_json(farmersmarkets)
        FROM farmersmarkets
        """

    # Executes query
    db_cursor = db.session.execute(QUERY)
    # Fetchall outputs each dictionary in a tuple
    rows = db_cursor.fetchall()

    for row in rows:
        # Append the first (dictionary) item of each tuple in the list of markets
        markets['markets'].append(row[0])

    return markets


def get_market_by_id(fm_id):

    markets = { 'markets': [] }

    QUERY = """
        SELECT row_to_json(farmersmarkets)
        FROM farmersmarkets
        WHERE fm_id = :fm_id
        """

    # Executes query
    db_cursor = db.session.execute(QUERY, {'fm_id': fm_id})
    # Fetchone outputs a dictionary in a tuple
    market = db_cursor.fetchone()
    # Append market to markets dictionary
    markets['markets'].append(market[0])

    return markets
