Simple Banking System in Python

This Python script demonstrates a simple banking system with classes for basic account operations. It includes a BankAccount class, a RewardAccount subclass, and a SavingsAcct subclass.
Usage

    Clone the Repository:

    bash

git clone https://github.com/mradegboyega/banking-system-python.git
cd banking-system-python

Run the Script:

bash

    python main.py

    Follow the Prompts:
        The script initializes several accounts with different balances.
        It performs deposit, withdrawal, and transfer operations.
        It demonstrates the use of a RewardAccount with a reward factor and a SavingsAcct with an additional fee.

Classes and Features
1. BankAccount

    Initialization:
        Creates a bank account with an initial balance and account name.

    Methods:
        get_balance: Displays the current balance.
        deposit(amount): Deposits money into the account.
        viableTransaction(amount): Checks if a transaction is viable.
        withdraw(amount): Withdraws money from the account.
        transfer(amount, account): Transfers money to another account.

2. RewardAccount (Subclass of BankAccount)

    Additional Feature:
        Provides a reward based on a reward factor.

    Method Override:
        deposit(amount): Extends the deposit method to include a reward.

3. SavingsAcct (Subclass of RewardAccount)

    Additional Feature:
        Includes an additional fee for withdrawals.

    Method Override:
        withdraw(amount): Extends the withdrawal method to account for the fee.

Contributing

Contributions are welcome! If you find a bug or have an enhancement in mind, feel free to open an issue or submit a pull request.
