#looping in dictionaries

accounts = {'name1':'password0','name2':'password1','name3':'password3'}

username = input('username: ')
password = input('password: ')

if username in accounts.keys():
  if password == accounts[username]:
    print('Welcome') 
  elif password != accounts[username]:
    print('Invalid Credentials')
  else:
    print('User not recognized.')