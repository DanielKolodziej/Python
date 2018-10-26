class Employee:
    raise_amount = 1.04 #class variable
    num_emps = 0
    def __init__(self, first, last, pay): #constructer
        self.first = first #instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount) # or Employee.raise_amount

    @classmethod     #needed in order to create class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #needed for static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1= Employee('Corey','Schafer',50000)
emp_2= Employee('Test','User',60000)

print(emp_1.email)
print(emp_1.fullname())
#same as above^^^
print(Employee.fullname(emp_1))

#####################
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#print(emp_1.__dict__) #prints variables in dictionary
emp_1.raise_amount= 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)

print(Employee.num_emps)

#####################################class methods

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1='john-doe-70000'
emp_str_2='setve-smith-30000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

###################################static method
import datetime
my_date = datetime.date(2018, 7, 10)
print(Employee.is_workday(my_date))
