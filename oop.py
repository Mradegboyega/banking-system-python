from bank_account import BankAccount, RewardAccount, SavingsAcct

Ade = BankAccount(150000, "Ade")
Toyin = BankAccount(15000, "Toyin")
Michelle = BankAccount(51000, "Michelle")
Gboyega = BankAccount(500000, "Gboyega")

Gboyega.get_balance()
Toyin.get_balance()

Michelle.deposit(20000)

Ade.withdraw(10000)

Toyin.transfer(10000, Michelle)
Toyin.transfer(10000, Ade)

Adekunle = RewardAccount(2000, "Adekunle")
Adekunle.get_balance()
Adekunle.deposit(500)
Adekunle.transfer(150, Ade)
Ade.get_balance()

emmanuel = SavingsAcct(1000, "emmanuel")
emmanuel.get_balance()
emmanuel.deposit(10000)
emmanuel.transfer(1500, Ade)
emmanuel.transfer(10000, Toyin)
