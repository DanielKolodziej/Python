#Daniel Kolodziej
#1/24/2018
#Lab 1  ITMD-413

import time

#local variable declaration
totalCost = 0.0

#Gather user input for first appliance and calculate its charge
appliance1 = input('please enter the appliance name: ')
cost1 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage1 = int(input('please enter the annual usage (in KW - hr): '))
charge1 = (cost1 * annUsage1)

#Gather user input for second appliance and calculate its charge
appliance2 = input('please enter the appliance name: ')
cost2 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage2 = int(input('please enter the annual usage (in KW - hr): '))
charge2 = (cost2 * annUsage2)

#Gather user input for third appliance and calculate its charge
appliance3 = input('please enter the appliance name: ')
cost3 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage3 = int(input('please enter the annual usage (in KW - hr): '))
charge3 = (cost3 * annUsage3)

#Gather user input for fourth appliance and calculate its charge
appliance4 = input('please enter the appliance name: ')
cost4 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage4 = int(input('please enter the annual usage (in KW - hr): '))
charge4 = (cost4 * annUsage4)

#Gather user input for fifth appliance and calculate its charge
appliance5 = input('please enter the appliance name: ')
cost5 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage5 = int(input('please enter the annual usage (in KW - hr): '))
charge5 = (cost5 * annUsage5)

#Gather user input for sixth appliance and calculate its charge
appliance6 = input('please enter the appliance name: ')
cost6 = float(input('please enter the cost per KW - hr of the appliance (in cents): '))
annUsage6 = int(input('please enter the annual usage (in KW - hr): '))
charge6 = (cost6 * annUsage6)

#adding all individual charges into total
totalCost = (charge1 + charge2 + charge3 + charge4 + charge5 + charge6)
print('The total cost of the annual usage is $','%.2f' % totalCost)

#author, date, time, lab number
print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab1')
