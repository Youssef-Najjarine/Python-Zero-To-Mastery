
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
