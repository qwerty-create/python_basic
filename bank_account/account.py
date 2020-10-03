class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>-self.min_balance:
            self.balance-=amount
        else:
            print("sorry, not enough balance")
    def statment(self):
        print("acount balance-{}: -> £{}".format(self.name,self.balance))

class Current_Account(Account):
    def __init__(self,name,balance):
        super(). __init__(name,balance,min_balance=200)
    def __str__(self):
        return "{'{}s current account £{}}".format(self.name,self.balance)

class SavingAccount(Account):
    def __init__(self,name,balance):
        super(). __init__(name,balance,min_balance=0)
    def __str__(self):
        return"{'s current account £{}".format(self.name,self.balance)
rohan_account=Current_Account("rohan",800)
rohan_account.deposit(300)
rohan_account.statment()
rohan_account.withdraw(50)
rohan_account.statment()