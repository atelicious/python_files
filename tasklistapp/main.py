#this will be the main for tasklistapp

import login_api, temporarydb, os, db_functions
from time import sleep
from user import User

#initial main menu for the app
def banner():
  print('='.ljust(29,'='))
  print('TaskListApp'.center(30))
  print('='.ljust(29,'='))

def main_menu(user):
  print('Welcome ' + str(user))
  print('\n1. View current Tasks\n2. Create new task\n3. Modify existing tasks\n4. Delete task(s)\n5. Logout\n6. Exit program')

def validate_text_input(input):
  input = input.strip().lower()
  if input == 'y':
    return 'y'
  elif input == 'n':
    return 'n'
  else:
    return 'invalid'

def validate_num_input(input, range):
  input = input.strip()
  try:
    input = int(input)
    if range[0] <= input <= range[1]:
      return input
  except:
    return 'invalid'

def clear_screen():
  #os.system('cls') -> Windows
  #os.system('clear') -> linux/macos
  os.system('clear')

def get_tasks(user):
  current_tasks = db_functions.get_user_username(user)[4]
  if current_tasks == '':
    print('There are no current tasks for you today')
  else:
    count = 0
    modified_tasks = current_tasks.split('***')
    if len(modified_tasks) > 1:
      print('These are your tasks for today: \n')
    else:
      print('This is your tasks for today: \n')
    for tasks in modified_tasks:
      print(f'{count + 1}. {tasks.title()}')
      count += 1

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
    main_menu(current_user)
    ask_input = input('Your choice? (1-5): ')
    ask_input = validate_num_input(ask_input, [0,6])
    
    if ask_input == 1:
      #view user tasks
      print('1')
      get_tasks(current_user)
      
    elif ask_input == 2:
      #add user tasks
      print('2')
      
    elif ask_input == 3:
      #modifying existing tasks
      print('3')

    elif ask_input == 4:
      #delete tasks
      print('4')

    elif ask_input == 5:   
      #logout user
      confirm_input = input('Do you want to log out? (y/n): ')
      confirm_input = validate_text_input(confirm_input)
      if confirm_input == 'y':
        login_state = False
        login_counter = 5
        current_user = None
        clear_screen()
      elif confirm_input == 'n':
        clear_screen()
        continue
      else:
        print('invalid input, please try again')
        continue
        
    elif ask_input == 6:
      #exit program
      main_loop = False
      print('6')
      
    else:
      #wrong input
      print('An error occured, please try again.')
  
  # break