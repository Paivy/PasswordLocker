import string
from random import * 
from user import User
from credentials import Credentials

def create_user(firstname,lastname,username,userpassword):
    newuser = User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()


def display_users():
    return User.display_user()

def create_account(accountusername,accountname,accountpassword):
    newaccount = Credentials(accountusername,accountname,accountpassword)
    return newaccount

def save_account(account):
    account.save_account()

def delete_account(account):
    account.delete_account()

def display_accounts():
    return Credentials.display_account()

def find_credentials():
    return Credentials.find_credentials()
def main():
    while True: