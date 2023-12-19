class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        """
        Initialize a bank account with an initial balance and account name.
        """
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nbalance = ${self.balance:.2f}")

    def get_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        self.balance += amount
        print("\nDeposit Successful! ✅")
        self.get_balance()

    def viableTransaction(self, amount):
        """
        Check if a transaction (withdrawal or transfer) is viable based on the account balance.
        """
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, {self.name}. You only have a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")

    def transfer(self, amount, account):
        """
        Transfer money from this account to another account.
        """
        try:
            print('\n**********\n\nTransfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Successful! 🙌\n\n**********')
        except BalanceException as error:
            print(f"Transfer Interrupted: {error}")


class RewardAccount(BankAccount):
    REWARD_FACTOR = 1.05  # Define the reward factor as a constant

    def deposit(self, amount):
        """
        Deposit money into a reward account, providing a reward based on the reward factor.
        """
        reward_amount = amount * self.REWARD_FACTOR
        self.balance += reward_amount
        print("\nDeposit Complete! ✅")
        self.get_balance()

class SavingsAcct(RewardAccount):
    def __init__(self, initialAmount, acctName):
        """
        Initialize a savings account as a type of reward account with an additional fee.
        """
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        """
        Withdraw money from a savings account, accounting for an additional fee.
        """
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawal completed. 😒")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")
