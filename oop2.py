"""Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:

It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
A method called get_balance that returns the current account balance.
A method called get_account_holder that returns the name of the account holder."""



class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder

if __name__ == "__main__":
    account = BankAccount("Wijdan", 100)
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Balance: {account.get_balance()}")
    
    account.credit(50)
    print(f"Balance after deposit: {account.get_balance()}")

