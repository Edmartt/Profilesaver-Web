import unittest
from flask import current_app
from app import create_app
from app.users import User


class TestUserMethods(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_set_password(self):
        user = User(username=None, password='1234')
        self.assertTrue(user.password_hash is not None)

    def test_forbbiden_password_get(self):
        user = User(username=None, password='1234')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_equals(self):
        user = User(username=None, password='1234')
        self.assertTrue(user.verify_password('1234'))
        self.assertFalse(user.verify_password('12345'))

    def test_password_salt_randomness(self):
        user = User(username=None, password='1234')
        user2 = User(username=None, password='1234')
        self.assertTrue(user.password_hash != user2.password_hash)
