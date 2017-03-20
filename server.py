from flask import Flask, render_template, redirect
from flask_restful import reqparse, abort, Resource, Api
from flask_debugtoolbar import DebugToolbarExtension
import jinja2

from model import *
from db_queries import *


app = Flask(__name__)
api = Api(app)

# jinja debugger
app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def homepage():
    """ Brings user to the homepage. """
    return render_template('index.html')


def error_if_nonexistent(fm_id):
    """ Returns an error message if farmer's market id is not found. """
    fm_ids = get_market_ids()
    if fm_id not in fm_ids:
        abort(404, message='Farmer\'s Market {} not found'.format(fm_id))


class MarketListAPI(Resource):
    """ Resource for full list of farmer's markets. """
    def get(self):

        return get_markets()
        # return ''


class MarketAPI(Resource):
    """ Resource for individual farmer's markets. """
    def get(self, fm_id):
        error_if_nonexistent(fm_id)
        # return markets[fm_id]
        pass

    def delete(self, fm_id):
        error_if_nonexistent(fm_id)
        return '', 204

    def put(self, fm_id):
        error_if_nonexistent(fm_id)
        pass



# Set up the API resource routing
api.add_resource(MarketListAPI, '/markets')
api.add_resource(MarketAPI, '/markets/<fm_id>')
# api.add_resource(Market, '/markets/<state_id>')



if __name__ == '__main__':
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # Connect DB to Flask before running app
    connect_to_db(app)

    app.run(host='0.0.0.0', port=5000, debug=True)
