#this will be the main for tasklistapp

import login_api, temporarydb, os
from time import sleep

#initial main menu for the app
def banner():
  print('='.ljust(29,'='))
  print('TaskListApp'.center(30))
  print('='.ljust(29,'='))

def clear_screen():
  #os.system('cls') -> Windows
  #os.system('clear') -> linux/macos
  os.system('clear')

def get_tasks(user):
  current_tasks = temporarydb.task_db[user]
  for tasks in current_tasks:
    print(tasks + '\n')

def add_tasks(user):
  new_task = input('Add your new task here: ')
  try:
    temporarydb.task_db[user].append(new_task)
  except:
    print('An error occured, please try again')

def modify_task(user):
  index = int(input('Your choice(1-'+str(len(temporarydb.task_db[user]))+')'))
  modified_task = [input('Add your modified task here: ')]
  a = temporarydb.task_db[user]
  b = a[:index-1] + modified_task + a[index:]
  temporarydb.task_db[user] = b

def delete_task(user):
  index = int(input('Your choice(1-'+str(len(temporarydb.task_db[user]))+')'))
  try:
    a = temporarydb.task_db[user]
    b = a[:index-1] + a[index:]
    temporarydb.task_db[user] = b
  except:
    print('An error occured, please try again')
#rewriting main loop

main_loop = True

while main_loop == True:
  #run main banner here
  banner()
  #check for positive login
  login_state = False
  login_counter = 5
  current_user = None

  while login_state == False and login_counter != 0:
    credentials = login_api.ask_credentials()
    if login_api.check_correct_credentials(credentials) == True:
      login_state = True
      print('Login successful, redirecting to main page.')
      current_user = credentials[0]
      sleep(5)
      clear_screen()
      break
    else:
      login_counter = login_counter -1
      print('Wrong credentials.')
      
    if login_state == False and login_counter == 0:
      print('You are blocked for 5 minutes')
      break

  while login_state == True:
    banner()
    print('Welcome ' + str(current_user))
    break
  
  break