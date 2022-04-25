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