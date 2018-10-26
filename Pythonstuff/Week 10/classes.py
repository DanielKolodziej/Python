
#Ex. 1- creating bank account with Global state
#
#problem: model is only good for one account holder!
'''
balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

deposit(1000)
withdraw(200)

print ("\nSingle Deposit ex. \nCur balance" ,balance)

balance = 200

print ("Updated balance" , balance)  

'''
'''
#Ex 2-
#Solution: creating model for multiple accounts
#
#make the state local, using a dictionary perhaps to store the state

def create_account():
    return {'balance': 0}  #return dictionary

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = create_account()
b = create_account()

print ("\nDeposits into multiple accounts: ")
print (deposit(a, 100))
print (deposit(b, 50))

print
print ("Withdrawals from multiple accounts: ")
print (withdraw(b, 10))

print (withdraw(a, 10))
 

 
#pickle dict object to file
import pickle

#use with statement to open, manipulate, close out file within block!
with open('bankAccts.pickle', 'wb') as f:
    pickle.dump(a, f)
   

#unpickle dict object from file

with open('bankAccts.pickle', 'rb') as f:
    dict_contents=pickle.load(f)

#print dict contents 

print ("\nPickeled Account:")
for k,v in dict_contents.items():     #display dictionary items
    print (k, ":" , v)
'''
 
#Ex 3
#using class as an example
class BankAccount:
    def __init__(self,name):
        self.balance = 0
        self.name=name;

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
a = BankAccount("a")
b = BankAccount("b")
a.deposit(100)
b.deposit(50)
b.withdraw(10)
a.withdraw(10)
 
 
#interpreting data by pickling list object to file
import pickle

data=[a,b]
#use with statement to open, manipulate, close out file within block!
with open('bankAccts.pickle', 'wb') as f:
    pickle.dump(len(data), f)
    for value in data: #loop thru each account holder
        pickle.dump(value,f) #save multiple accounts to pickled file
 
#unpickle object listing from file
data2=[]
with open('bankAccts.pickle', 'rb') as f:
    for _ in range(pickle.load(f)):
        data2.append(pickle.load(f))

#print list contents 
print ("\nBalance on file: ", data2[0].balance,'\n') #nice but how to know if index 0 is a certain account like a or b... 


#alternative use shelves to save multiple objects by key (object name)
#serves as a database!

import shelve

dbase=shelve.open('accts')    #make new shelve
for obj in (a,b):             #store objects
    dbase[obj.name]=obj       #use name for key    

dbase.close();

#retrieve values from database
dbase=shelve.open('accts')    #reopen shelve

print ("Database keys:",list(dbase.keys()))
print ("Database object A reference:",dbase['a'])
print ("Database object B:",dbase['b'].balance)
'''
'''
'''
#Ex. 4 - other shelve example
import shelve

flights = {"1":"A", "2":"B", "3":"C"}
times = ["230pm", "320pm", "420pm"]

db = shelve.open('shelved','n')  #flags/modes can be c,n,r or w
                                 #https://docs.python.org/2/library/dbm.html#module-dbm

db['flights'] = flights
db['times'] = times

print (db.keys())

db.close()

# Retrieving Objects from a Shelve File

db = shelve.open('shelved','r')

for k in db.keys():
    obj = db[k]
    print ("Vals %s: %s" % (k, obj))

flightDB = db['flights']
flights = flightDB.keys()
cities = flightDB.values()
times = db['times']

for flights,cities in flightDB.items():
    print ("Flight %s leaves for %s at %s" %(flights,cities,times[int(flights)-1]))

db.close()

'''
    





