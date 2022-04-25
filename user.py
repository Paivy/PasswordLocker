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
       
    def save_user(self):
        """
        save_user method saves user info into the user list
        """
        User.userslist.append(self)
    def delete_user(self):
        """
        delete_user method deletes a saved user from the userslist
        """
        User.userslist.remove(self)
