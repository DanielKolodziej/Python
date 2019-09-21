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


class Student:

    def __init__(self, name, major, gpa, onProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.onProbation = onProbation

    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


student1 = Student('Dan', 'Information Technology', 3.7, False)
student2 = Student('Joe', 'Information Technology', 1.7, True)
print(student2.gpa)
print(student1.honor_roll())
