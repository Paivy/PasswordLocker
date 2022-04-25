import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_account = Credentials("Paivy","paivy123","paivy123")

    def tearDown(self):
        Credentials.accounts = []

