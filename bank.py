
class Account: 
    def __init__(self,username = 'Darpan'): 
        self.balance=0
        self.username = username
        print(f'Hello!!! {self.username} Welcome to the Deposit & Withdrawal Machine') 
        
        if self.balance == 0:
            print("Insufficient amount please add amount")
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print(f'\n Amount Deposited:',amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print(f'\n Net Available Balance= {self.balance}',) 
  
d = Account() 
   
d.deposit() 
d.withdraw() 
d.display()
