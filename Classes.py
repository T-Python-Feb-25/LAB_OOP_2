
class BankAccount:
    def __init__(self, account_holder: str, initial_balance=0):
        self.__account_holder = account_holder
        self.__initial_balance = 0
        self.deposit(initial_balance)

    def get_balance(self):
        return f"{self.__account_holder} balance is {self.__initial_balance}"

    def get_account_holder(self):
        return f"the account holder is  {self.__account_holder}"


    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError(f"amount {amount} not allowed it must be greater than zero")

        self.__initial_balance += amount
        return f"Amount {amount} added successfully to {self.__account_holder}.\nNew balance: {self.__initial_balance }"

    def withdraw(self, amount: int):

        if self.__initial_balance < amount:
            raise ValueError("Insufficient funds")

        else:
            self.__initial_balance -= amount

        return f"{self.__account_holder} Withdrawal successful\nNew Balance {self.__initial_balance}"



