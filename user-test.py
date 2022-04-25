import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Paivy","paivy123")