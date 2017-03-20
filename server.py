from flask import Flask, render_template, redirect
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
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


@app.route('/api')
def api_details():
    """ Brings user to the API. """
    return render_template('api.html')

class Markets(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Markets, '/markets')

# @app.route('/api/markets')


# @app.route('/api/markets/<fmid>')


# @app.route('/api/markets/<state>')


if __name__ == '__main__':
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=5000, debug=True)
