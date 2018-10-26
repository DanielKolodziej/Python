#Daniel Kolodziej
#2/18/2018
#Lab 4  ITMD-413

import time
import random

#declare variable for user attempts
tries = 2

#create a random list of 3 "winning" numbers between 0 and 9
lottolist = sorted(random.sample(range(0, 10), 3))
#print (lottolist) #-> just for testing purposes
#fireball value	
fireball = random.randint(0,9)
#print (fireball) #-> just for testing purposes

#ask whether user want the fireball option included
game = input('You are playing pick3 lotto game, would you like to add the fireball option? [y/n]')
#loop to continue as long as user still has tries left (3 total)
while (tries >= 0):
    while True:
        #Error catch to prevent negative, non-numeric, and longer than one digit values for first guess
        while True:
            try:
                num1 = int(input('Enter in your first number choice (0-9): '))
                if ((len(str(num1))) != 1):
                    print('One positive digit only! Try again')
                else:
                    break
            except ValueError:
                    print('Non-numeric data input.')
        #Error catch to prevent negative, non-numeric, and longer than one digit values for second guess
        while True:
            try:
                num2 = int(input('Enter in your second number choice (0-9): '))
                if ((len(str(num2))) != 1):
                    print('One positive digit only! Try again')
                else:
                    break
            except ValueError:
                    print('Non-numeric data input.')
        #Error catch to prevent negative, non-numeric, and longer than one digit values for third guess
        while True:
            try:
                num3 = int(input('Enter in your third number choice (0-9): '))
                if ((len(str(num3))) != 1):
                    print('One positive digit only! Try again')
                else:
                    break
            except ValueError:
                    print('Non-numeric data input.') 
        #create a list with all three values given by user
        uList = [num1, num2, num3]

        #function checker that compares the lotto numbers to user list and returns whether they match
        def checker():
            if uList == lottolist:
                return True
            else:
                return False
        #function fChecker for fireball mode to compare list with fireball replacement
        def fChecker():
                if uList == lottolist:
                    return True
                elif fList1 == lottolist:
                    return True
                elif fList2 == lottolist:
                    return True
                elif fList3 == lottolist:
                    return True
                else:
                    return False
        #if user chose n, fireball is ignored
        if (game == 'n'):
            #if checker comes back true, user has won, stop program
            if checker() == True:
                print('Congratulations! A $100 cash prize will be coming your way soon!')
                print('The lucky numbers were', lottolist)
                print('Your choices were', uList)
                tries = -1
            #if checker comes back false, update tries and ask whether they would like to continue
            else:
                print('Nice try, better luck next time around!')
                print('Your choices were', uList)
                print('You have', tries, 'attempt(s) left')
                if (tries > 0):
                    again = input('Would you like to try again? [y/n]')
                    while True:
                        if (again == 'y'):
                            tries = tries -1
                            break
                        elif (again == 'n'):
                            print('Good luck and come back soon!')
                            tries = -1
                            break
                        else:
                            again = input('Invalid, Do you wish to try again? [y/n]: ')
                #user has run out of attempts, display winning numbers, stop program
                else:
                    print('You have run out of attempts, the winning numbers were', lottolist)
                    tries = -1
            break
        #if user chose y, fireball is included
        elif (game == 'y'):
            #list with fireball replacing each option
            fList1 = [fireball, num2, num3]
            fList2 = [num1, fireball, num3]
            fList3 = [num1, num2, fireball]

            if fChecker() == True:
                print('Congratulations! You won with Fireball, bonus $50 earned for a total of $150!')
                print('The lucky numbers were', lottolist)
                print('Your choices were', uList)
                print('The fireball was', fireball)
                tries = -1
            else:
                print('Nice try, better luck next time around!')
                print('Your choices were', uList)
                print('You have', tries, 'attempt(s) left')
                if (tries > 0):
                    again = input('Would you like to try again? [y/n]')
                    while True:
                        if (again == 'y'):
                            tries = tries -1
                            break
                        elif (again == 'n'):
                            print('Good luck and come back soon!')
                            tries = -1
                            break
                        else:
                            again = input('Invalid, Do you wish to try again? [y/n]: ')
                else:
                    print('You have run out of attempts, the winning numbers were', lottolist)
                    print('The fireball was', fireball)
                    tries = -1
            break
        else:
            game = input('Invalid, would you like to add the fireball option? [y/n]')
#author, date, time, lab number
print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab4')


