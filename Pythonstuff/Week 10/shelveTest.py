from classes import *

#shelving example furthered
#https://docs.python.org/2/library/shelve.html

import shelve

#retrieve values from database
dbase=shelve.open('accts')    #reopen shelve

print (list(dbase.keys()))
'''
print (dbase['a'])
print (dbase['b'].deposit(1));    #beware of mutation!!!
print (dbase['b'].balance);       #no writeback switched by default
'''
