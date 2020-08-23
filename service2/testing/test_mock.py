from flask import url_for
import unittest
from flask_testing import TestCase
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
    def test_getclass_view(self):

        response = self.client.get(url_for('get_class'))
        self.assertEqual(response.status_code, 200)




