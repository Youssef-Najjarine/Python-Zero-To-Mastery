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
