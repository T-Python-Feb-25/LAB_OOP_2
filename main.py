from BankAccount import BankAccount
try: 

  account2 = BankAccount("Omar waleed", 100)
  if account2.exists:
      print(f" account in account holder is {account2.get_account_holder()}")
      print(f"account in initial_balance is {account2.get_balance()}")

  else:
     print(f"New account created: {account2.get_account_holder()} - balance is: {account2.get_balance()}")
     print(f" account in account holder is {account2.get_account_holder()}")
     print(f"account in initial_balance is {account2.get_balance()}")
  

  
  account2.deposit(50)
  print(f"Balance after deposit : {account2.get_balance()}")
  
  account2.withdraw(20)
  print(f"Balance after withdraw {account2.get_balance()}")

except Exception as e:
  print(f"You have error in deposit or in withdraw: {e}")

