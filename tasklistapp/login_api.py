#do the login for the app first
import temporarydb
from db_functions import get_user_pw, get_user_by_username, create_user
from user import User


def ask_credentials():
  username = input('username: ')
  password = input('password: ')

  return (username, password)

def get_new_credentials(new_username,new_password):
  new_username = new_username
  new_password = new_password

  return (new_username, new_password)

#check for username uniqueness, if unique = true, otherwise false
def check_for_unique_username(new_username):
  if not get_user_by_username(new_username):
    return True
  else:
    return False

def add_new_credentials(new_username,new_password, new_fname, new_lname):
  new_user = User(new_username,new_password, new_fname, new_lname, '')
  create_user(new_user)

def check_correct_credentials(credentials):
  if not get_user_by_username(credentials[0]):
    return False
  else:
    if credentials[1] in get_user_pw(credentials[0]):
        return True
    else:
      return False
