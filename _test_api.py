import unittest

from server import app
from model import *




class ApiEndpointTests(unittest.TestCase):
    """ Tests API endpoints. """

    def setUp(self):
        """ Sets up a new client before each test. """

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, db_uri='postgresql:///farmersmarkets-testdb')
        db.create_all()


    def test_homepage(self):
        """ Tests homepage exists. """

        result = self.client.get('/')
        self.assertIn('<h1>API for farmer\'s markets in the U.S.</h1>', result.data)


    def test_markets(self):
        """ Tests /markets endpoint works. """

        result = self.client.get('/markets')
        self.assertEqual(200, result.status_code)


    def test_market_id(self):
        """ Tests /market/<fm_id> endpoint works. """

        result = self.client.get('/market/abc')
        self.assertEqual(404, result.status_code)
        self.assertIn('Farmer\'s market abc is not a valid format. Use digits only.', result.data)

    def test_market_state(self):
        """ Tests /market/<fm_id> endpoint works. """

        result = self.client.get('/market/ca')
        self.assertEqual(200, result.status_code)


    def tearDown(self):
        """Drop database after every test."""

        db.session.close()
        db.drop_all()



if __name__ == '__main__':

    unittest.main()
