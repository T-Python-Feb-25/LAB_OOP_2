"""
Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:

It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
A method called get_balance that returns the current account balance.
A method called get_account_holder that returns the name of the account holder.
"""
import json
import os 
class BankAccount:
    FILE_NAME = "accounts.json"
    def __init__(self, account_holder: str, initial_balance=0.0):
        if self.__account_exists(account_holder):
            self.__account_holder = account_holder
            self.__load_account()
            self.__exists = True 
            print(f"Account already exists: {account_holder} - balance is: {self.__balance}")

        else:
            
            self.__account_holder = account_holder
            self.__balance = float(initial_balance)
            self.__save_account()
            self.__exists = False 
            print(f"New account created: {account_holder} with balance: {self.__balance}")

    def exists(self):
        return self.__exists


    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        
        self.__balance += amount
        self.__save_account()
        print(f"Deposited: {amount}. New balance: {self.__balance}")
        return self.__balance


    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self.__save_account()
        return self.__balance  
        print(f"Withdrew: {amount}. Remaining balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder
    
    def __save_account(self):
        data = self.__load_data()
        data[self.__account_holder] = {"balance": self.__balance}

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def __load_account(self):
        data = self.__load_data()
        if self.__account_holder in data:
            self.__balance = data[self.__account_holder]["balance"]

    @classmethod
    def __load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
        return {}
    
    def __account_exists(self, account_holder):
        data = self.__load_data()
        return account_holder in data






        



  
