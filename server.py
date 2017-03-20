from flask import Flask, render_template, redirect
from flask_restful import reqparse, abort, Resource, Api
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


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
    # markets =
    if fm_id not in markets:
        abort(404, message='Farmer\'s Market {} not found'.format(fm_id))


class MarketList(Resource):
    def get(self):
        return {'hello': 'world'}


class Market(Resource):
    def get(self, fm_id):
        error_if_nonexistent(fm_id)
        # return markets[fm_id]

    def delete(self, fm_id):
        error_if_nonexistent(fm_id)
        return '', 204

    def put(self, fm_id):
        error_if_nonexistent(fm_id)
        # return



# Set up the API resource routing
api.add_resource(MarketList, '/markets')
api.add_resource(Markets, '/markets/<fm_id>')


# @app.route('/api/markets/<state>')


if __name__ == '__main__':
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=5000, debug=True)
