class BankAccount:
    
    
    def __init__(self , account_holder,initial_balance=0 ):
        self.__account_holder=account_holder
        self.__balance=initial_balance
        # self.deposit(initial_balance)
    
        
    def deposit(self, amount):
        if not isinstance(amount, int):
            raise Exception(" amount must be number")
        elif amount>0:
            self.__balance +=amount
            return self.__balance
        else:
            raise Exception(" amount must be greater than zero.")
        
        
            
    def get_balance(self):
        return self.__balance 
    
    def get_account_holder(self):
        return self.__account_holder
    
    
    
    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise Exception(" amount must be number")
        elif amount>=0 and amount<= self.__balance:
            self.__balance -=amount
            return self.__balance
        
        else:
            raise Exception("amount must be greater than zero , The withdraw amount greater than balance Account !!")  
         
        
        
            
          
        
        
        
        
    

        
        