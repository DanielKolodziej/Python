class BankAccount(object):
    rate = .02
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
    def getBalance(self):
        return self.balance 
    
    @staticmethod
    def setRate(rate):
    	BankAccount.rate=rate;
    @staticmethod
    def getRate():
    	return BankAccount.rate;

my_account = BankAccount(15)
my_account.withdraw(5)

print ("\nSingle account holder amt: $",my_account.balance, sep="")

BankAccount_objs = [
        BankAccount(65),
        BankAccount(50),
        ]

for index in range(len(BankAccount_objs)):
    print("\nList of account holder amts-> (Holder %d) $" % (index+1), BankAccount_objs[index].getBalance(),sep="");
print("\nCurrent bank rate:         "  , str(BankAccount.rate).strip('0'),sep="")
BankAccount.rate=.04
print("\nUpdated bank rate 1:       ", str(BankAccount.rate).strip('0'),sep="")
BankAccount.setRate(.06);  
print("\nUpdated bank rate 2:       ", str(BankAccount.rate).strip('0'),sep="")
