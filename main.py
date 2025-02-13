from Classes import BankAccount


def main():
    try:
        account1 = BankAccount("Alice", 100)
        account2 = BankAccount("Bob", 500)

        print(account1.get_balance())
        print(account2.get_balance())

        print(account1.deposit(50))
        print(account2.deposit(200))

        print(account1.withdraw(30))
        print(account2.withdraw(100))

        print(account1.get_balance())
        print(account2.get_balance())

        print(account1.withdraw(5000))
        print(account2.deposit(-20))

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
