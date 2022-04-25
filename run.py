#!/usr/bin/env python3.8

import string
from random import * 
from user import User
from credentials import Credentials

def create_user(username,userpassword):
    newuser = User(username,userpassword)
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
        print("Welcome to Password Locker write SU TO Signup or LG  to Loginto start")
        print("SU -or- LG")
        option=input()
        if option == "SU":
            print("Create Account")
            print("-"*10)
            print("Set your username ..")
            username = input()
            print("Set your password ..")
            userpassword = input()
            save_user(create_user(username,userpassword))
            print("Your account was created successfully.These are your acc details:")
            print("-"*10)
            print(f"Name:\nUsername: {username} \nPassword:{userpassword}")
            print("\nUser Login to your account with your details")
            print("\n \n")

        break
    while True:
        print("Use the following short codes: \n  cc - create credentials account \n dc- display creadentials \n fc - find credentials \n d - delete credentials")

        short_code = input()

        if short_code == 'cc':
            print('Create a credentials Account:')
            print('-'*10)
            print('Account Username...')
            accountusername = input()

            print('Account Name...')
            accountname = input()

            print('Account Password...')
            accountpassword = input()

        # elif short_code == 'dc':
            





        # break







if __name__ == '__main__':
    main()