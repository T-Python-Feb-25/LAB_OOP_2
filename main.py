from Lab import BankAccount
try:
    
    account = BankAccount("ghaida", 12000)
    print(account.deposit(100))  

    
    print(account.get_balance())  
    print(account.withdraw(50))
    print(account.get_balance())
    
    
except Exception as e:
    print(e)
