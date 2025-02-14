from Bank_oop import BankAccount

# Creating instances
account1 = BankAccount("Areej", 300000)
account2 = BankAccount("Nora", 10000)

print(account1.describe())
print(account2.describe())


account1.deposit(500)
account1.withdraw(300)
account2.deposit(200)
account2.withdraw(100)


print("\nAfter Transactions:")
print(account1.describe())
print(account2.describe())

account1.apply_interest()
account2.apply_interest()

print("\nAfter Interest Applied:")
print(account1.describe())
print(account2.describe())

print("\nTransaction History for Areej:")
for transaction in account1.get_transaction_history():
    print(f"{transaction['date']} - {transaction['type']} - {transaction['amount']}$")

print("\nAreej's Full Report:")
account1.generate_report()