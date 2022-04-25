import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Paivy","paivy123")
    def tearDown(self):
        User.userslist = []
    def test_init(self):
        self.assertEqual(self.new_user.username,"Paivy")
        self.assertEqual(self.new_user.password,"paivy123")
