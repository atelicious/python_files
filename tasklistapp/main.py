#this will be the main for tasklistapp

import login_api, temporarydb

#initial main menu for the app
print('='.ljust(29,'='))
print('TaskListApp'.center(30))
print('='.ljust(29,'='))


#check first for positive login 
login_state = False
login_counter = 5

while login_state == False and login_counter != 0:
  credentials = login_api.ask_credentials()
  if login_api.check_correct_credentials(credentials) == True:
    login_state = True
    print('Login successful, redirecting to main page.')
    break
  else:
    login_counter = login_counter -1
    print('Wrong credentials.')

if login_state == False and login_counter == 0:
  print('You are blocked for 5 minutes')

while login_state == True:
  print('welcome')
  break