#Daniel Kolodziej
#1/24/2018
#Lab 2  ITMD-413

import time

#local variable declaration
bmi = 0.0

#Gather user input for weight and height
weight = float(input('please enter your weight ( in pounds U.S. ): '))
height = float(input('please enter your height ( in inches U.S. ): '))

#calculate bmi
bmi = ((weight * 703)/ height**2)
print('You have a bmi of', '%.2f' % bmi)

#Print weight status according to bmi
if (bmi < 18.5):
    print('You are Underweight')
elif (bmi >= 18.5 and bmi <= 25):
    print('You are normal weight')
else:
    print('You are Overweight')

#author, date, time, lab number
print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab2')
