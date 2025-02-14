from datetime import datetime

class BankAccount:

    # Constructor
    def __init__(self, account_holder: str, initial_balance: float = 0.0, withdrawal_fee: float = 1.0, minimum_balance: float = 100.0, interest_rate: float = 0.05):
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__withdrawal_fee = withdrawal_fee  # Withdrawal fee
        self.__minimum_balance = minimum_balance  # Minimum balance to maintain
        self.__interest_rate = interest_rate  # Interest rate for monthly interest
        self.__transaction_history = [] #List to store transection


    #method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction("Deposit", amount)
            return self.__balance
        else:
            raise Exception("Deposit amont must be greater then 0")
        
        
        
    def withdraw(self, amount: float) -> float:
        total_amount = amount + self.__withdrawal_fee  # Total withdrawal amount including fee
        if total_amount > self.__balance:
            raise Exception("Insufficient funds!")
        if self.__balance - total_amount < self.__minimum_balance:

            raise Exception(f"Cannot withdraw, minimum balance of {self.__minimum_balance}$ must be maintained!")
        self.__balance -= total_amount

        self.__add_transaction("Withdrawal", amount)  # Add transaction to history
        return self.__balance
    
    def __add_transaction(self, type: str, amount: float):
        transaction = {
            "type": type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.__transaction_history.append(transaction)

    
    def get_transaction_history(self):
        return self.__transaction_history

    def apply_interest(self):
        if self.__balance > 0:
            interest = self.__balance * self.__interest_rate
            self.__balance += interest
            self.__add_transaction("Interest", interest)
    

    def get_balance(self) -> float:
        return self.__balance
    
    def get_account_holder(self) -> str:
        return self.__account_holder
    
    def generate_report(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}$")
        print("Transaction History:")
        for transaction in self.get_transaction_history():
            print(f"{transaction['date']} - {transaction['type']} - {transaction['amount']}$")
    
    def describe(self) -> str:
        return f"Account Holder: {self.get_account_holder()}, Balance: {self.get_balance()}$"
