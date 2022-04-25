
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

def find_credentials(accountname):
    return Credentials.find_credentials(accountname)

def check_existing_cred(accountname):
    """
    function to check for existing credentials
    """
    return Credentials.cred_exist(accountname)
chars = 'abcdefghijklmnoprstuvwyzABCDEFGHIKLMNOPRSTUVWYZ1234567890~`!@#$%^&*()?/[]'
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

            while True:
                print('use short code: \n own - enter your own password, gen - generate a password')
                short_code = input().lower()
                if short_code == 'own':
                    print('Password:')
                    accountpassword = input()
                elif short_code == 'gen':
                    while True:
                        password_len = int(
                        input('password length:'))
                        password = ''
                        for x in range(0, password_len):
                            password_char = random.choice(chars)
                            password = password + password_char
                            print('Hello here is your password:',accountpassword)
                        break
                    print('Password:')
                    accountpassword = input()
                break

            save_account(create_account(accountusername,accountname,accountpassword))

        elif short_code == 'dc':

            if display_accounts():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_accounts():
                    print(f"{credentials.accountname} \n {credentials.accountusername} \n{credentials.accountpassword}")

                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any accounts saved yet")
                print('\n')


        elif short_code == 'fc':
            print('Please Enter Account to Search:')
            search_account = input()
            if check_existing_cred(search_account):
                search_cred = find_credentials(search_account)
                print('\n')
                print(
                f'Yes you have {search_cred.accountname} in your storage.')
            else:
                print('Ooops!! That account does not exist!!')

        elif short_code == 'd':
            print('Please Enter Account to Delete:')
            search_account = input()
            if find_credentials(search_account):
                search_cred = find_credentials(search_account)
                search_cred.delete_account()        
                print('\n')
                print(
                    f'Your {search_cred.accountname} credentials were deleted successfully! ')
            else:
                print('Ooops!! That account does not exist!!')

    


if __name__ == '__main__':
    main()