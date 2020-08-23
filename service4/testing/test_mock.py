from flask import url_for
import unittest
from flask_testing import TestCase
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
    def test_postweapon_view(self):

        response = self.client.get(url_for('post_weapon'))
        self.assertEqual(response.status_code, 500)

    def test_weapon_knight(self):
        response = self.client.post('/post/weapon', data="Knight")
        self.assertIn(b'Sword', response.data)

    def test_weapon_warrior(self):
        response = self.client.post('/post/weapon', data="Warrior")
        self.assertIn(b'Axe', response.data)
    
    def test_weapon_hunter(self):
        response = self.client.post('/post/weapon', data="Hunter")
        self.assertIn(b'Bow', response.data)

    def test_weapon_mage(self):
        response = self.client.post('/post/weapon', data="Mage")
        self.assertIn(b'Staff', response.data)

    def test_weapon_pyro(self):
        response = self.client.post('/post/weapon', data="Pyro")
        self.assertIn(b'Flame', response.data)
