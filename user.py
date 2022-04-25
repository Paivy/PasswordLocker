import random
import string

class User:
    """
    This is a class that generates instances of the class
    """
    userslist=[]

    def __init__(self,username,password):
        """
        __init__ method helps us define properties for our objects which is self
        """
        
        self.username=username
        self.password=password
       
