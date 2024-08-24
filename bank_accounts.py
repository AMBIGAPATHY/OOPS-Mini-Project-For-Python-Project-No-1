class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialamount,accname):
        self.balance=initialamount
        self.name=accname
        print(f"\nAccount '{self.name}' created.\nbalance = ${self.balance:.2f}")
        
    def getbalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance}")    
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getbalance()
    
    def transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance}"
            )        
    
    def withdraw(self,amount):
        try:
            self.transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw intrupted:{error}")
          
    def transfer(self,amount,account):
        try:
            print("\n****\n\nBegining transfer..")
            self.transaction(amount)          
            account.deposit(amount)
            print("\ntransfer complete! \n\n****")
        except BalanceException as error:
            print(f"\nTransfer intreupted..{error}")
            
class IntrestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getbalance()
        
class SavingsAccount(IntrestRewardAcc):
    def _init_(self, initialamount, accname):
        super()._init_(initialamount, accname)
        self.fees=5
    
    def withdraw(self, amount):
        try:
            self.transaction(amount+self.fees)
            self.balance = self.balance - (amount + self.fees)
            print("\nWithdraw completed.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithraw interupted:{error}")