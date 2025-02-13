from classes import BankAccount

account1 = BankAccount("Elaf", 1000)
account2 = BankAccount("Jana")

print(account1.get_balance())
print(account2.get_balance())

print(account1.deposit(500))
print(account2.deposit(1000))

print(account1.get_account_holder())
print(account2.get_account_holder())

try:
    account1.withdraw(50)
except ValueError as e:
    print(e)
        
