import json
from validator import validate_email
import validator
import time
import datetime
'''
multiline comment
'''
# single line comment

x = 1  # int
y = 2.5  # float
name = 'daniel'  # str
is_boolean = True  # boolean
x, y, name, is_cool = (1, 2.5, 'Daniel', True)  # multiple assignment

print('Hello')  # print statement

x = str(x)  # casting
y = int(y)


# concatenate
myName = 'Dan'
age = 22
phrase = 'longer sentence for nothing'
nums = '12345'
print('Hello, my name is {myName}. I am {age}.'.format(myName=myName, age=age))


# f-strings (3.6+) -> use command    Py -3 filename.py
# print(f'Hello, my name is {myName} and I am {age}')

print(name.capitalize())  # only first letter
print(name.upper())  # all letters
print(name.lower())  # lower all letters
print(name.swapcase())  # switch case
print(len(name))  # get length
print(name.replace('iel', '123'))  # replace
print(name.count('a'))  # count occurance
print(name.startswith('hello'))  # return true or false
print(name.endswith('goodbye'))  # return true or false
print(phrase.split())  # split into a list
print(name.find('n'))  # return position
# only checks strings
print(nums.isalnum())  # return true or false if contains letters or num
print(name.isalpha())  # return true or false if contains letters
print(phrase.isnumeric())  # return true or false if contains nums


# a list is a collection which is ordered and changeable. allows duplicates
numbers = [1, 2, 8, 3, 4, 5]
# use contructer
numbers2 = list((1, 2, 3, 4))
fruits = ['apple', 'orange', 'grape', 'raspberry', 'blackberry', 3]
#print(fruits[0])
print(fruits[1:3])#prints indexes 1-2 (including till 3 excluding)
fruits[0] = 'blueberries'
#print(len(fruits))
fruits.append('mangos')  # add to end of list
fruits.remove('grape')  # remove element
fruits.insert(1, 'banana')  # insert specific position
fruits.pop(2)  # remove specific index
fruits.reverse()  # reverse the list
numbers.sort()  # sort list ascending
print(fruits)
print(numbers)


# tuple is collection which is ordered but UNCHANGEABLE, allows duplicate
# leave trailing comma if only 1 val...  one = (1,)
fruits2 = ('strawberry', 'kiwi', 'lemon')
del fruits2  # delete tuple


# set is a collection which is unordered and unindexed, NO DUPLICATES
# wont return error if trying to add duplicate, just wont do change
fruits_set = {'apple', 'orange', 'melon'}
print('apple' in fruits_set)  # check if val in set, prints true or false
fruits_set.add('grape')  # add to set
fruits_set.remove('grape')  # remove from set
fruits_set.clear()  # clears set, makes empty, can use del to remove entirely


# dictionary =collection unordered, changeable, and indexed. No Duplicates
person = {
    'first_name': 'Dan',
    'last_name': 'Kolo',
    'age': 30
}
print(person)
# use construction
person2 = dict(first_name='Joe', last_name='Shmoe', age=30)
# get value
print(person['first_name'])
print(person.get('last_name'))
# add key/value
person['phone'] = '555-555-555'
# get dict keys
print(person.keys())
# get dict items
print(person.items())
# copy dict
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)
# remove key/value
del(person['age'])
person.pop('phone')

# list of dictionaries
people = [
    {'name': 'Martha', 'age': 20},
    {'name': 'Kev', 'age': 26}
]

'''
user input -> always returns string
'''
userName = input("What is your name?")
userAge = input("What is your age?")
print("Hi, " + userName + ". You are " + userAge)


# function is a block of code which only runs when called
def sayHello(name='Sam'):  # can add default value
    print(f'Hello {name}')
sayHello('Dan Kolo')


def getSum(num1, num2):
    total = num1+num2
    return total


num = getSum(4, 2)
print(num)


'''
lambda function is a small anonymous function, can take any num of parameters
but only have one expression
'''


def getSum2(num1, num2): return num1+num2


print(getSum2(19, 2))


# if statement, elif, else, nested
x = 10
y = 20
x2 = 10
if x > y:
    print(f'{x} is greater than {y}')
    if x - y == 10:
        print(f'{x} - {y} is 10')
elif x == y:
    print(f'{y} is equal to {x}')
else:
    print(f'{y} is greater than {x}')


# logical operators
if x > y and y <= 30:
    print(f'{x} is greater than {y} and {y} is less or equal to 30')
if x > y or y <= 30:
    print(f'{x} is greater than {y} or {y} is less or equal to 30')
if x > y and not(y <= 30):
    print(f'{x} is greater than {y} and {y} is not less or equal to 30')


# membership operators (in, not in) used to test if sequence is presented
number5 = [7, 8, 9, 10, 11]
if x in number5:
    print(x in number5)
if y not in number5:
    print(y not in number5)


# identity operators (is, is not) compare objects if they are the same object
# with the same memory location
if x is x2:
    print(x is x2)
if x is not y:
    print(x is not y)


# for loop iterate over a sequence that is list, tuple, dict, set, or string
pies = ['chicken', 'apple', 'cherry']
for pie in pies:
    print(f'Current pie: {pie}')
    # can break out of loop with      break
    # can continue with (will skip to next )       continue

for i in range(len(pies)):
    print(pies[i])
for i in range(0, 11):
    print(f'Number: {i}')

# while loop
count = 0
while count <= 4:
    print(count)
    count += 1

'''
try block of code, except(catch) the if error occurs, can chain except
'''
try: numb = int(input("enter a number: "))
    print(numb)
except ValueError:
    print("invalid input")
except ZeroDivisionError as err: #store error in variable
    print(err)


'''
a module is basically a file containing a set of funcrions to include 
in your app.  There are core modules, modules ucan install using the pip
package manager--(like npm)-- (including Django) as well as custom modules
for example ----->  pip install camelcase
'''
# core modules
# if only want specific from module
#from datetime import date

# pip module
#from camelcase import CamelCase

today = datetime.date.today()
timestamp = time.time()

'''
c = CamelCase()
print(c.hump('hello there world'))
'''

print(today)
print(timestamp)

# import custom module

email = 'test@yahoo.com'
if validate_email(email):
    print('email is valid')
else:
    print('not valid')

'''
a class is a blueprint for creating objects, an object has properties
and methods(functions) associated with it
'''


class User:
    # constructer
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# extend class


class Customer(User):
    # constructer
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# init user object
brad = User('Brad Traversy', 'btrav@google.com', 37)
print(brad.name)
brad.has_birthday()
print(brad.greeting())

# init customer object
janet = Customer('Janet Johnson', 'janet@test.net', 25)
janet.set_balance(500)
print(janet.greeting())


'''
python has functions for creating, reading, updating, and deleting files
r = read, w = write, a = append, r+ = read and write
'''

# open a file
myFile = open('myFile.txt', 'w')
# get info on file
print('Name: ', myFile.name)
print('is closed: ', myFile.closed)
print('opening mode: ', myFile.mode)

# write to file
myFile.write('I wrote this to the file')
myFile.write('...also this')
myFile.close()

# append to file
myFile = open('myFile.txt', 'a')
myFile.write('This part is appended')
myFile.close()

# read from file
myFile = open('myFile.txt', 'r+')
test = myFile.read(10)
oneLine = myFile.readline()#stores the first line into variable
manyLines = myFile.readlines()#stores lines into variable as list
print(test)
myFile.close()


'''
JSON is commonly used with data APIS, parse JSON into python dictionary
'''
# sample json
userJSON = '{"first_name": "John", "last_name": "Doe"}'
# parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# turn dictionary to json
car = {'make': 'Ford', 'model': 'Mustang', 'year': 2002}
carJSON = json.dumps(car)
print(carJSON)
