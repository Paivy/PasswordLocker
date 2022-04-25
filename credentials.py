import random
import string
class Credentials:
    """
    This is a class that generates new instances of Credentials
    """ 
    accounts = []
    def __init__(self,accountusername,accountname,accountpassword):
        """
        __init__ method helps us define properties for our objectself.
        """
        self.accountusername   =accountusername
        self.accountname =accountname
        self.accountpassword = accountpassword

    def save_account(self):
        """
        save_account method saves user information in accounts
        """
        Credentials.accounts.append(self)
    def delete_account(self):
        """
        delete_account method deletes user information in accounts
        """
        Credentials.accounts.remove(self)
    @classmethod
    def display_account(cls):
        """
        method that returns information from the accounts
        """
        # for account in cls.accounts:

        return cls.accounts

    @classmethod
    def find_credentials(cls, account):
        """
         function to find credentials
        """
        
        for credentials in cls.accounts:
            if credentials.accounts == account:
                return credentials

    @classmethod
    def credentials_exist(cls, account):
        for credentials in cls.accounts:
            if credentials.account == account:
                return True
        return False