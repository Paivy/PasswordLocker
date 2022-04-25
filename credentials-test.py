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
    def test_save_user(self):
        self.new_account.save_account()
        self.assertEqual(len (Credentials.accounts),1)

    def test_delete_user(self):
        """
        test_delete_contact to test if we can remove an account from our accounts list
        """
        self.new_account.save_account()
        test_account = Credentials("Paivy","paivy123","paivy123")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len (Credentials.accounts),1)
    

  
        
    def test_display_user(self):
        self.assertEqual(Credentials.display_account(), Credentials.accounts)
        

if __name__ == '__main__':
    unittest.main()