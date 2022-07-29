

class BackAccount:
    def __init__(self):
        self.balance = 0
        print("Hello! Welcome to the Deposite and Withdrawal Machine ")

    def deposite(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited: ", amount)
    
    def withdrawal(self):
        amount = float(input("Enter amount to be Withdrawal: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew: ",amount)
        else:
            print("\n Insufficient Balance!")
    
    def display(self):
        print("\n Curret Balance: ", self.balance)

s = BackAccount()

s.deposite()
s.withdrawal()
s.display()