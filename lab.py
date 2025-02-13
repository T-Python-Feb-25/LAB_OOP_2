from classes import BankAccount



try:
    #account1 = BankAccount("Raed",1000)
    account2 = BankAccount("Raef")

    #print(account1.get_account_holder())
    print(account2.get_account_holder())

    #account1.deposit(400)

    #print(account1.get_balance())
    print(account2.get_balance())

    #account1.withdraw(300)
except Exception as ex : 
    print(ex)