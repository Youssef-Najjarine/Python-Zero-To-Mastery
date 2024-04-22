
name = input("What is your name?")
print('hellooooo ' + name)

#Fundamental Data Types
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(2 / 4,type(2 / 4))
print(9.9 + 1.1)
print(type(9.9 + 1.1))
print(2 ** 3)
print(2 // 3)
print(2 % 3)

#Math Functions
print('Round: ', round(3.1))
print('Absolute Value: ', abs(-20))

#Math Functions
print('Round: ', round(3.1))
print('Absolute Value: ', abs(-20))

#Operator Precedence
print((20 - 3) + 1 ** 4)

# ()
# **
# * /
# + -

user_iq = 190
user_age = user_iq/4
print(user_age)

#constants
PI = 3.14 #caps lets other programmers know variable shouldn't be changed

a,b,c = 1,2,3
print(a)
print(b)
print(c)

some_value = 5
some_value += 2

print('some_value: ', some_value)

username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
0 0
___
'''

print(username)
print(password)
print(long_string)

#Escape Sequences

weather = "\t It\'s \"kind of \" sunny \n hope you have a good day!"
print('weather: ', weather)

#formatted strings

name = 'Johnny'
age = 55
print('hi ' + name + '. You are ' + str(age) +  ' years old')
print('hi {}. You are {} years old'.format('Johnny', '55'))

print(f'hi {name}. You are {age} years old')

selfish = '01234567'
#string slicing [start:stop:stepover]
print(selfish[0:2])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::2])
print(selfish[-3])
print(selfish[::-1])

#Immutable strings selfish[0] = '8' doesn't work but selfish = selfish + 8 would add 8

greet = 'heloooo'
print(len(greet))
print(greet[0: len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))

print(bool(1))
print(bool(0))

birth_year = input('What year were you born?')
age = 2019 - int(birth_year)
print(f'Your age is: {age}')

user_name = input('What is your username?')
password = input(f'What is {user_name}\'s password?')
hidden_password = len(password) * '*'
print(f'{user_name}\'s password {hidden_password} is {len(password)} long')

li = [1,2,3,4,5,6,7,8,9,10]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

#List slicing
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix
matrix = [
  [1,2,3],
  [2,4,6],
  [7,8,9]
]
print(matrix[0][1])

basket = [1,2,3,4,5]

#adding
basket.append(100)
basket.insert(6,200)
basket.extend([300,400])
new_list = basket[:]
print('Adding: ',basket)
print('Adding: ',new_list)

#removing
basket.pop()
basket.pop(0) # we give index we want to remove with pop
basket.remove(4) # we give exact value of element we want to remove with remove

print('Removing: ',basket)

basket.clear()
print('Cleared: ',basket)

basket2 = ['a','x','b','c','d','e','d']
basket3 = sorted(basket2)
basket2.sort()
basket2.reverse()
print(basket2.index('d',0,5))
print('x' in basket2)
print('i' in 'hi my name is Ian')
print(basket2.count('d'))
print(basket2[::-1])
print(basket2)
print(basket3)
print(list(range(1,101)))

new_sentence = ' '.join(['hi','my','name','is','JOJO'])
print(new_sentence)

#List Unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9] #can be applie to tuples as well
print(a)
print(b)
print(c)
print(other)
print(d)

sen = 'Hi I am youssef'
split = sen.split(' ')
join = ' '.join(split)
print(split)
print(join)

weapons = None
print(weapons)

dictionary = {
  'a': [1,2,3],
  123: 'hello',
  True: True
}

my_list = [
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
  },
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
  },
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
  }
]
dictionary['my_name'] = 'ustes'
print(dictionary['a'][1])
print(dictionary[123])
print(dictionary[True])
print(dictionary)

user = {
  'basket': [1,2,3],
  'greet': 'HeLLo',
  'age': 30
}
print(user.get('age',55))
user2 = dict(JohnJohn='JohnJohn')
print(user2)
print('basket' in user)
print(user.items())

my_tuple = (1, 2, 3, 4, 5,5)
print (5 in my_tuple)
tupl_obj = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 27
}
print(tupl_obj[(1,2)])

new_tuple = my_tuple[1:2]

print(new_tuple)
print(my_tuple.count(5))
print(my_tuple.index(5))

my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)

my_list = [1,2,3,4,5,5]
print(set(my_list))
print(1 in my_set)
print(my_set)

#.difference()
#.discard()
#.difference_update()
#.intersection()
#.isdisjoint()
#.issubset()
#.issuperset()
#.union()

is_old = True
is_licenced = False

if is_old and is_licenced: print('you are old enough to drive!')
elif is_old or is_licenced:
  print('you can drive now!')
else:
  print('you are not of age!')

# if is_old & is_licenced: print('you are old enough to drive!')
# elif is_old | is_licenced:
#   print('you can drive now!')
# else:
#   print('you are not of age!')

# Ternary Operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

is_magician = False
is_expert = True

if is_magician and is_expert:
  print('you are a master is_magician')
elif is_magician and not is_expert:
  print('at least you are getting there')
elif not(is_magician):
  print('you need magic powers')

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

for item in [1,2,3,4,5]:
  for lttr in 'Zero to Mastery':
    print(item,lttr)

#iterable - list, dictionary, tuple, set, string

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}
for key,value in user.items():
  print(key,value)

for item in user.items():
  key, value = item
  print(item)
  print(key,value)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for item in user:
  print(item,user[item])

my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
counter = 0

for num in my_list:
  if isinstance(num, (int, float, complex)):
    counter += num
print(counter)

for el in range(0,10,2):
  print(el)
for _ in range(2):
  print(list(range(10)))

for i,char in enumerate((1,2,3)):
  print(i,char)

for i,char in enumerate(list(range(100))):
  if (char == 50):
    print(f'The index of 50 is: {i}')

i = 0
while i < 50:
  print(i)
  i += 1
else:
  print('done with all the work')

while True:
  response = input('say something: ')
  if (response == 'bye'):
    break
    # continue
    # pass

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

photo = ''
for arr1 in picture:
  for num in arr1:
    if (not(num)):
      photo +=' '
    elif (num):
      photo += '*'

  photo += '\n'

print(photo)
