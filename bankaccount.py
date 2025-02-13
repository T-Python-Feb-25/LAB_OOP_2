class BankAccount:
    def __init__(self,name,initial_balance=0):
        self.__account_holder=name
        self.__balance=0
        self.__balance=self.deposit(initial_balance)
    def deposit(self,amount):
        '''`deposit` a function that accepts an amount and adds it to the account balance, and then returns the updated balance.'''
        if amount>=0 and isinstance(amount,int):
            self.__balance+=amount
        else:
            raise Exception("invalid input enter a valid number")
        return self.__balance
    def withdraw(self,amount):
        '''`withdraw` a function that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged '''
        if amount<0 and not isinstance(amount,int):
            raise Exception("invalid input enter a valid number")
            

        if self.__balance < amount :
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
    




