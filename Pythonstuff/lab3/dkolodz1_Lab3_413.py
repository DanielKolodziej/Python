#Daniel Kolodziej
#2/07/2018
#Lab 3  ITMD-413

import time

#local variable declaration
balance = 0.0
interest = 0.0
tries = 2
cont = 0

#create user pin, try-except to prevent non-numeric values
#also check if pin is 4 digits
while True:
        try:
            pinSet = int(input('Create your desired 4 digit pin number: '))
            if ( (len(str(pinSet))) != 4):
                print('Pin length entered was not 4 digits, try again')
            else:
                print('Pin Creation Successful')
                break
        except ValueError:
            print('Non-numeric data input.')


#loop to track user attempts and compare the chosen pin to the one that is entered
while (tries >= 0) :
    
    pinCheck = int(input('please enter your 4 digit pin number: '))

    if (pinCheck == pinSet):
        tries = -1
        print('Login Successful')

        #loop to continue based on user input
        #(if n = update and stop), (if y = reset balance), else (does not except non-numeric value)
        while (cont == 0):
            #try-except to catch non-numeric input for balance
            while True:
                try:
                    initial = float(input('please enter your initial bank account balance: '))
                    break
                except ValueError:
                    print('Non-numeric data input.')
            #try-except to catch non-numeric input for interest
            while True:
                try:
                    rate = float(input('please enter your annual interest rate ( as a decimal ): '))
                    break
                except ValueError:
                    print('Non-numeric data input.')
            #calculate balance
            balance = balance + initial
            start = 1
            stop = 12
            #loop calculation for 12 months
            for count in range(start, stop + 1) :  
                interest = balance * ( rate / 12 )  
                balance += interest
                print ("Month: ", count, " New Monthly Balance: $", '%.2f' % balance)

            #ask user input to continue
            again = input('Do you wish to try again? [y/n]: ')
            while True:
                if (again == 'n'):
                    cont = cont + 1
                    break
                elif (again == 'y'):
                    cont = cont + 0
                    balance = 0.0
                    break
                else:
                    again = input('Invalid, Do you wish to try again? [y/n]: ')
#update user attempt value and display when incorrect
    else:
        print('Incorrect pin, you have', tries, 'attempt(s) left')
        tries = tries - 1


#author, date, time, lab number
print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab3')

