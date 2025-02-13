from classes import BankAccount

try:

    account1 = BankAccount("Nawaf Alahmadi")
    account2 = BankAccount("Naif Alahmadi",15000)

    # Account One
    account1.deposit(1000)
    print(account1.get_account_holder())
    print(account1.get_balance())
    account1.withdraw(1000)
    print(account1.get_balance())
    # 
    print("-"*20)
    # Account Two
    print(account2.get_account_holder())
    print(account2.get_balance())
    account2.deposit(10000)
    print(account2.get_balance())
except Exception as e:
    print(e)