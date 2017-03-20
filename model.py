from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()



##### PostgreSQL Tables #####


class HasItem(db.Model):
    """ Yes, No, or No Data """

    __tablename__ = 'hasitems'

    has_item_id = db.Column(db.String(10), primary_key=True, nullable=False)
    has_item = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        """ Shows information about the item. """
        return '<HasItem id=%s>' % (self.has_item_id)


class State(db.Model):
    """ State abbreviations and data. """

    __tablename__ = 'states'

    state_id = db.Column(db.String(2), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        """ Shows information about the user. """

        return '<State id=%s name=%s>' % (self.state_id, self.name)


class FarmersMarket(db.Model):
    """ Farmer's markets information. """

    __tablename__ = 'farmersmarkets'


    fm_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    website = db.Column(db.String(2083), nullable=True)
    facebook = db.Column(db.String(500), nullable=True)
    twitter = db.Column(db.String(500), nullable=True)
    youtube = db.Column(db.String(500), nullable=True)
    other_media = db.Column(db.String(500), nullable=True)
    street = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    county = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(2), db.ForeignKey('states.state_id'), nullable=False)
    zipcode = db.Column(db.String(15), nullable=True)
    season_1_date =  db.Column(db.String(200), nullable=True)
    season_1_time =  db.Column(db.String(200), nullable=True)
    season_2_date =  db.Column(db.String(200), nullable=True)
    season_2_time =  db.Column(db.String(200), nullable=True)
    season_3_date =  db.Column(db.String(200), nullable=True)
    season_3_time =  db.Column(db.String(200), nullable=True)
    season_4_date =  db.Column(db.String(200), nullable=True)
    season_4_time =  db.Column(db.String(200), nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    latlng = db.Column(Geometry(geometry_type='POINT'), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    credit = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    wic = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    wic_cash = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    sfmnp = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    snap = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    organic = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    baked_goods = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    cheese = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    crafts = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    flowers = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    eggs = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    seafood = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    herbs = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    vegetables = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    honey = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    jams = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    maple = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    meat = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    nursery = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    nuts = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    plants = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    poultry = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    prepared = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    soap = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    trees = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    wine = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    coffee = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    beans = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    fruits = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    grains = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    juices = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    mushrooms = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    pet_food = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    tofu = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    wild_harvested = db.Column(db.String(10), db.ForeignKey('hasitems.has_item_id'), nullable=False)
    date_updated = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """ Shows information about the farmer's market. """
        return '<FarmersMarket id=%s name=%s>' % (self.fm_id, self.name)



##### PostgreSQL connection and db setup #####

def connect_to_db(app, db_uri='postgresql:///farmers-markets'):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # Import app from server if opening from this file
    from server import app

    connect_to_db(app)
    print "Connected to DB."

    # In case tables haven't been created, create them
    db.create_all()
