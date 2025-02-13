'''# LAB_OOP_2

Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged 
(make sure to handle the exception when calling the method).
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

---------
'''
class BankAccount:
    def __init__(self,name,initial_balance=0):
        self.__account_holder=name
        self.__balance=initial_balance
    def deposit(self,amount):
        '''`deposit` a function that accepts an amount and adds it to the account balance, and then returns the updated balance.'''
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        '''`withdraw` a function that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged '''
        if self.__balance < amount:
            raise Exception(f"Can't withdraw {amount}, it is greater than current balance of {self.__balance}.")
        else:
            self.__balance-=amount
            return self.__balance
        
    def get_balance(self):
        '''`get_balance` a function that returns the current account balance.'''
        return self.__balance
    def get_account_holder(self):
        ''' `get_account_holder` a function that returns the name of the account holder'''
        return self.__account_holder






        