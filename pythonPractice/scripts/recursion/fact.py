#Program which accepts a number from the user
#take the numbers 0 to the number input 
#and gives a total of the numbers

def main():
#Get the number from the user to define upper end of range
              num = int(input('Enter a non-negative integer: '))

#Create the list of numbers
              fact = factorial(num)
              print(fact)

def factorial(num):
              if num == 0:
                  return 1
              else:
                  return num * factorial(num-1)
#call the main function
main() 
