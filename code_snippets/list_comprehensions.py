#code snippets for common list comprehensions in python

num_list = [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]

#condition = give 'n' for each 'n' in num_list
# using a normal for loop:
my_list = []
for n in num_list:
  my_list.append(n)
print(my_list)

#using list comprehensions
my_list = [n for n in num_list]
print(my_list)

#condition = give 'n*n' for each 'n' in num_list
#using normal for loop
my_list = []
for n in num_list:
  my_list.append(n*n)
print(my_list)

#using normal list comprehensions
my_list = [n*n for n in num_list]
print(my_list)

#using map + lambda
mylist = map(lambda n: n*n, num_list)
print(my_list)

#condition = give 'n' for each 'n' if 'n' is even
#using normal for loop
my_list = []
for n in num_list:
  if n%2 == 0:
    my_list.append(n)
print(my_list)

#using normal list comprehension
my_list = [n for n in num_list if n%2 == 0]
print(my_list)

#using a filter + lambda
my_list = filter(lambda n: n%2 == 0, num_list)
print(my_list)

#condition = give a (letter, number) pair for each letter in 'abcd' each number in '0123'
#using normal for loop
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append(letter, num)
print(my_list)

#using list comprehensions
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

#for dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# normal for loop
my_dict = {}
for name, hero in zip(names, heros):
  my_dict[name] = hero
print(my_dict)

#using dictionary comprehensions
my_dict = {name:hero for name, hero in zip(names, heros)}
print(my_dict)

#additional condition = name is not equal to 'Peter'
my_dict = {name:hero for name, hero in zip(names, heros) if name != 'Peter'}

#for set comprehensions
#using normal for loop
my_set = set()
for n in num_list:
  my_set.add(n)
print(my_set)

#using set comprehension
my_set = {n for n in num_list)}
print(my_set)

#generator expressions
#condition = yield 'n*n' for each 'n' in num_list

def gen_func(nums):
  for n in nums:
    yield n*n

my_gen = gen_func(num_list)

for i in my_gen:
  print(i)