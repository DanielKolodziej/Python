#Daniel Kolodziej
#4/1/2018
#ITMD-413 - Lab8
'''
a.	A function to create a table
b.	A function to update a table
c.	A function to delete from a table
d.	A function to insert into a table
e.	A function to read (load in) record(s) from a table
When referring to or creating a table use contacts as your database name.
Your database table name will be your first name. 

'''
import sqlite3

# Open database connection

conn = sqlite3.connect('contacts.db')
print ("Opened database successfully");

class myDatabasefile:
    pass
