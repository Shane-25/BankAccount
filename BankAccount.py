# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}, Balance: {self.balance}')
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

accountA = BankAccount(0.01, 2500)
accountB = BankAccount(0.05, 8000)

accountA.deposit(15).deposit(1000).deposit(20).withdraw(500).yield_interest().display_account_info()
accountB.deposit(250).deposit(300).withdraw(1000).withdraw(200).withdraw(2000).withdraw(3000).yield_interest().display_account_info()
