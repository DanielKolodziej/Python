#Program which accepts a number from the user
#take the numbers 0 to the number input 
#and gives a total of the numbers

def main():
#Get the number from the user to define upper end of range
              num = int(input('Enter a non-negative integer: '))

#Create the list of numbers
              numbers = list(range(1,num+1))
              print(numbers)
#Get the sum of the list of numbers
              my_sum = range_sum(numbers, 0, len(numbers)-1)

#Display the total
              print('The sum of 1 to', num, 'is: ', my_sum)

def range_sum(num_list, start, end):
              if start > end:
                  return 0
              else:
                  return num_list[start] + range_sum(num_list, start+1, end)
#call the main function
main() 
