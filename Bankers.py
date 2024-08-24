from bank_accounts import *

sarath=BankAccount(1000, "sarath")
kumar=BankAccount(2000, "kumar")

sarath.getbalance()
kumar.getbalance()

sarath.deposit(5000)

sarath.withdraw(1000)

sarath.transfer(1000,kumar)
sarath.transfer(100, kumar)

akbar=IntrestRewardAcc(1000, "akbar")
akbar.getbalance()
akbar.deposit(100)
akbar.transfer(100,sarath)

arun=SavingsAccount(1000, "arun")
arun.getbalance()
arun.deposit(100)
arun.transfer(10000,kumar)
arun.transfer(1000,kumar)