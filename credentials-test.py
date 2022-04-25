import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_account = Credentials("Paivy","paivy123","paivy123")

    def tearDown(self):
        Credentials.accounts = []

    def test_init(self):
        self.assertEqual(self.new_account.accountusername,"Paivy")
        self.assertEqual(self.new_account.accountname,"paivy123")
        self.assertEqual(self.new_account.accountpassword,"paivy123")
        