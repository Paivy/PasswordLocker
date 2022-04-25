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
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Paivy","paivy123")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.userslist),1)




    """
    Test class that defines testcases for the user class behaviours
    Args:
    unittest.Testcase: TestCase class that helps in creating testcases
    """
if __name__ == '__main__':
    unittest.main()
