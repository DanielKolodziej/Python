class Employee():

    def __init__(self, first_name, last_name, annual_salary = 3000):
        """Declare the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_default_raise(self):
        """Add $5,0000 by default to the annual salary, but accept any amount"""
        self.annual_salary += 5000
        new_salary = self.annual_salary
        print("Default raise:",new_salary)

    def give_custom_raise(self):
        """Add a custom amount"""
        custom_raise = input("How much would you like to increase? ")
        self.annual_salary += int(custom_raise)
        new_custom_salary = self.annual_salary
        print("\nCustom raise:",new_custom_salary)
       
accountant = Employee('John', 'Jones')
#accountant.give_default_raise()

import unittest

class TestEmployee(unittest.TestCase):
    '''Note that the order in which the various test cases will be run is
    determined by sorting the test function names with respect to the
    built-in ordering for strings'''
    """Test the Employee class"""
    def setUp(self):
        #create a new employee
        self.accountant = Employee('John', 'Jones', 120000)
         
        
    def test_give_default_raise(self):
        # give him a default raise
        self.accountant.give_default_raise()

        # verify that the salary was increased by the expected amount
        self.assertEqual(self.accountant.annual_salary, 125000)
        
    def test_give_custom_raise(self):
        # create a new employee
        self.accountant = Employee('John', 'Jones', 120000)

        # give him a default raise
        self.accountant.give_custom_raise()

        # verify that the salary was increased by the expected amount
        self.assertEqual(self.accountant.annual_salary, 130000)
        
unittest.main()
