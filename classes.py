class BankAccount:
    def __init__(self,account_holder:str , initial_balance:float = 0):
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.deposit(initial_balance)

    def deposit (self,amount:float):
        if not isinstance(amount,int):
            raise Exception("amount must be a number")
        if amount < 0:
            raise Exception("the amount must be can 0")
        self.__balance += amount
        
    
    def withdraw(self,amount:float):
        if amount > self.__balance:
            raise Exception("no funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder