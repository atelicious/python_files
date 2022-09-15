import sqlite3

conn = sqlite3.connect('user_db.db')

c = conn.cursor()

#initialize main user table with 5 columns (username, password, firstname, password)

try:
  c.execute("""CREATE TABLE user_table (username text password text fname text lname text tasks text) """)
except sqlite3.OperationalError:
  pass

#create methods for user registration

#search db by username
def get_user_by_username(username):
  with conn:
    c.execute("SELECT * FROM user_table WHERE username =:username",{'username':username})
  return c.fetchall()

#create a new user

def create_user(user):
  with conn:
    c.execute("INSERT * FROM user_table VALUES (:username, :password, :fname, :lname, :tasks", {'username':user.username, 'password':user.password, 'fname':user.fname, 'lname':user.lname}, 'tasks':'' )

#search user by username (will be used for username checking)

def get_user_username(username):
  with conn:
    c.execute("SELECT * FROM user_table WHERE username =:username", {'username':username})
  return c.fetchone()

#get user password for login verification

def get_user_pw(username):
  with conn:
    c.execute("SELECT password FROM user_table WHERE username =:username", {'username':username})
  return c.fetchone()

#methods for updating data in profile
  
#for updating user's first name
def update_fname(username, new_fname):
  with conn:
    c.execute("UPDATE user_table SET fname =:new_fname WHERE username =:username ", {'username':username, 'fname':new_fname})

#for updating user's last name
def update_lname(username, new_lname):
  
  

  
  


