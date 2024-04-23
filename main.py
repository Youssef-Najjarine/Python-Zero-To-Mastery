
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

picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

photo = '\n'
for arr1 in picture:
  for num in arr1:
    if (not (num)):
      photo += ' '
    elif (num):
      photo += '*'

  photo += '\n'


def say_hello(name, emoji):
  print(f'hellooooo {name} {emoji}')


print(say_hello)
say_hello('Youssef', photo)

def checkDriverAge(age=0):
  age = age

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!")
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

checkDriverAge(21)

# Docstrings

def test(a):
    '''
    Info: this function tests and prints param a.
    '''
    print(a)

test('a')

# *args **kwargs

def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs

def highest_even(li):
  even_nums = []
  for num in li:
    if (num % 2 == 0):
      even_nums.append(num)

  even_nums.sort()
  return even_nums[len(even_nums) - 1]

print(highest_even([10,2,3,4,8,11]))

a = 'helloooooooooo'

if ((n := len(a)) > 10):
  print(f"too long {n} elements")

while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]

print(a)

a = 1

def confusion():
  a = 5
  return a

print(confusion())
print(a)

total = 0

def count(total):
  total += 1
  return total

# count()
# count()
# print(count())
print(count(count(count(total))))
