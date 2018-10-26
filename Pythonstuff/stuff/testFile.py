import time
import os

def menu() :
   pstr = "Choose from the following payroll choices\n"
   pstr += "(1) A gross PR payroll report for all employees\n"
   pstr += "(2) A gross PR payroll report for a single employee by name\n"
   pstr += "(3) Add an employee\n"
   pstr += "(4) Delete an employee\n"
   pstr += "(5) Modify an employee\n"
   pstr += "(6) Quit Program"
   print (pstr)

def printAll():
    empFile = open("testEmp.txt", "r")
    for line in empFile :
        empInfo = line
        empInfoSplit = empInfo.split(" ")
        f = empInfoSplit[0]
        l = empInfoSplit[1]
        r = float(empInfoSplit[2])
        h = float(empInfoSplit[3])
        gross = r * h
        employeeResult = [f,l,'$%.2f' % gross]
        print(employeeResult)
    print('---All users printed')
    
def printEmp():
    empFile = open("testEmp.txt", "r")
    found = False
    #checks if user input was atleast 1 character, with stripping spaces
    while True:
       search = input("Enter first name to search an employee: ")
       search2 = input("Enter last name to search an employee: ")
       if len(search.strip()) < 1 or len(search2.strip()) < 1:
          print('Error, User input was less than 1 character')
       else:
          break
    search = search.strip()
    search2 = search2.strip()
    for line in empFile:
        if (search in line) and (search2 in line):
            found = True
            search = line
    if found == True:
        empInfoSplit = search.split(" ")
        f = empInfoSplit[0]
        l = empInfoSplit[1]
        r = float(empInfoSplit[2])
        h = float(empInfoSplit[3])
        gross = r * h
        employeeResult = [f,l,'$%.2f' % gross]
        print(employeeResult)
        print('---Record has printed')
    else:
        print('Employee,', search, search2, ',does not exist')
    
def addEmp():
    empFile = open("testEmp.txt", "a")
    #checks if user input was atleast 1 character, with stripping spaces
    while True:
       fName = input("Enter in your first name: ")
       lName = input("Enter in your last name: ")
       if len(fName.strip()) < 1 or len(lName.strip()) < 1:
          print('Error, User input was less than 1 character')
       else:
          break
    fName = fName.strip()
    lName = lName.strip()
    while True:
        try:
            rate = float(input("Enter in your rate of pay: "))
            hour = float(input("Enter in your hours worked: "))
            if rate < 0 or hour < 0:
                print('Values cannot be less than 0...')
            else:
                break
        except ValueError:
            print('Non numeric data input, Try again...') 
    newEmployee = ['\n',fName, ' ', lName, ' ', str(rate), ' ', str(hour)]
    empFile.writelines(newEmployee)
    print('---User,', fName, lName,',has been added')
    
def deleteEmp():
    found = False
    empFile = open("testEmp.txt", "r")
    lines = empFile.readlines()
    empFile.close()
    #checks if user input was atleast 1 character, with stripping spaces
    while True:
       search = input("Enter first name to delete an employee: ")
       search2 = input("Enter last name to delete an employee: ")
       if len(search.strip()) < 1 or len(search2.strip()) < 1:
          print('Error, User input was less than 1 character')
       else:
          break
    search = search.strip()
    search2 = search2.strip()
    for line in lines:
       if (search in line) and (search2 in line):
          found = True
    if found == True:
       empFile = open("testEmp.txt", "w+")
       for line in lines:
          if (search not in line) and (search2 not in line):
             empFile.write(line)
       print('---User,', search, search2,',has been deleted')

    else:
       print('Employee,', search, search2, ',does not exist')
              
def modifyEmp():
    found = False
    empFile = open("testEmp.txt", "r")
    lines = empFile.readlines()
    empFile.close()
    #checks if user input was atleast 1 character, with stripping spaces
    while True:
       search = input("Enter first name to modify an employee: ")
       search2 = input("Enter last name to modify an employee: ")
       if len(search.strip()) < 1 or len(search2.strip()) < 1:
          print('Error, User input was less than 1 character')
       else:
          break
    search = search.strip()
    search2 = search2.strip()
    for line in lines:
       if (search in line) and (search2 in line):
           found = True
    if found == True:
        empFile = open("testEmp.txt", "w+")
        for line in lines:
           if (search not in line) and (search2 not in line):
               empFile.write(line)
           elif (search in line) and (search2 in line):
               while True:
                   try:
                       rate = float(input("Enter in your rate of pay: "))
                       hour = float(input("Enter in your hours worked: "))
                       if rate < 0 or hour < 0:
                           print('Values cannot be less than 0...')
                       else:
                           break
                   except ValueError:
                       print('Non numeric data input, Try again...')
               fName = search
               lName = search2
               modEmployee = [fName, ' ', lName, ' ', str(rate), ' ', str(hour),'\n']
               empFile.writelines(modEmployee)
               print('---File has been updated...')
    else:
       print('Employee,', search, search2, ',does not exist')
            
    
def exitApp():
    print('---Your program will now close, Goodbye...')
    exit()

def main() :
   empFile = open("testEmp.txt", "r")
   while True:
       try:
           menu()
           choice = int(input("Enter Menu Choice [1-6] "))
           if choice == 1 :
            printAll()
           elif (choice == 2) :
            printEmp()
           elif (choice == 3) :
            addEmp()
           elif (choice == 4) :
            deleteEmp()
           elif (choice == 5) :
            modifyEmp()
           elif (choice == 6) :
            exitApp()
           else:
            print('Option not available, try again...')
       except ValueError:
            print ("Non numeric data input, Try again...")
   empFile.close()

main()

