from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app


    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()



class TestResponse(TestBase):
    def test_homepage_view(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_generatepage_view(self):

        response = self.client.get(url_for('generate'))
        self.assertEqual(response.status_code, 200)


    def test_postpage_view(self):

        with requests_mock.mock() as g:
            g.get("http://service2:5001/get/class", text="Warrior")
            g.get("http://service3:5002/get/race", text="Human")
            g.post("http://service4:5003/post/weapon", text="Axe")
            response = self.client.get(url_for('generatehero'))
            self.assertEqual(response.status_code, 200)




