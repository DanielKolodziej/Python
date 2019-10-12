from re import *
 
'''*******************great reference site**********************

https://www.tutorialspoint.com/python/python_reg_expressions.htm

*************************************************************'''
 
pattern = compile( '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)' )

def get_address() :

	address = input( 'Enter Your Email Address: ' )

	is_valid = pattern.match( address )

	if is_valid :
		print( 'Valid Address:' , is_valid.group() )
	else:
		print( 'Invalid Address! Please Retry...\n' )
		get_address()

get_address()
 
