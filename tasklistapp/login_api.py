#do the login for the app first
import temporarydb


def ask_credentials():
  username = input('username: ')
  password = input('password: ')

  return (username, password)

def get_new_credentials(new_username,new_password):
  new_username = new_username
  new_password = new_password

  return (new_username, new_password)

def check_for_unique_username(new_username):
  if new_username in temporarydb.accounts.keys():
    return True
  else:
    return False

def add_new_credentials(new_username,new_password):
  try:
    temporarydb.accounts.append(new_username,new_password)
  except:
    print('An error occured, registration failed')
  else:
    print('Registration successful')

def check_correct_credentials(credentials):
  if credentials[0] in temporarydb.accounts.keys():
    if credentials[1] == temporarydb.accounts[credentials[0]]:
      return True
    else:
      return False
  else:
    return False

