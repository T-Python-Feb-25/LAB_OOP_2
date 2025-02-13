class BankAccount:
    def __init__(self, account_holder:str, balance:float = 0):
        self.__account_holder = account_holder
        self.__balance = 0
        self.deposit(balance)

    # Methods
    def deposit(self, amount:float):
        if not isinstance(amount, int):
            raise Exception("Enter Number Chars not accepted")
        if amount < 0:
            raise Exception("Enter Vlaue Above 0")

        self.__balance += amount
    
    def withdraw(self, amount:float):
        if amount > self.__balance:
            raise Exception("No Enough funds.")
        self.__balance -= amount 

    def get_account_holder(self):
        return self.__account_holder
    def get_balance(self):
        return self.__balance
