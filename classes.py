'''
LAB_OOP_2
Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:

It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
A method called get_balance that returns the current account balance.
A method called get_account_holder that returns the name of the account holder.
'''
class BankAccount:
    def __init__(self, account_holder_name: str, initial_balance: float = 0) -> None:
        self.__account_holder_name = account_holder_name
        self.__balance = initial_balance

    def deposit(self, amount: float) -> float:
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount:float) -> float:
        if amount > self.__balance:
            raise Exception("Insufficient funds, Process can't be completed")
        self.__balance -= amount
        return self.__balance     
        
    def get_balance(self) -> float:
        return self.__balance
    
    def get_account_holder(self) -> str:
        return self.__account_holder_name





        