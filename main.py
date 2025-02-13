from bankaccount import BankAccount
ahmed_account=BankAccount("ahmed",1000)
try:
    ahmed_account.withdraw(10000)
except Exception as e:
    print(e)

print(ahmed_account.get_balance())
khaild_account=BankAccount("khaild",1000)
print(khaild_account.deposit(100))
try:
    print(khaild_account.withdraw(1000))
except Exception as e:
    print(e)

print(khaild_account.get_account_holder())
print(khaild_account.get_balance())

