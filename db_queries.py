from server import *
from model import *


def get_market_ids():
    """ Gets full list of farmer's market ids. """
    fm_ids = set()

    markets = db.session.query(FarmersMarket.fm_id).all()
    for m_id in markets:
        fm_ids.add(m_id[0])

    return fm_ids


def get_state_ids():
    """ Gets full list of state ids. """
    state_ids = set()

    markets = db.session.query(State.state_id).all()
    for s_id in markets:
        state_ids.add(s_id[0])

    return state_ids


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
    """ Gets farmer's market by id. """

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


def get_market_by_state(state_id):
    """ Gets farmer's market by state. """

    markets = { 'markets': [] }

    QUERY = """
        SELECT row_to_json(farmersmarkets)
        FROM farmersmarkets
        WHERE state = :state
        """

    # Executes query
    db_cursor = db.session.execute(QUERY, {'state': state_id.upper()})
    # Fetchall outputs a each dictionary item in a tuple
    rows = db_cursor.fetchall()

    for row in rows:
        # Append market to markets dictionary
        markets['markets'].append(row[0])

    return markets

