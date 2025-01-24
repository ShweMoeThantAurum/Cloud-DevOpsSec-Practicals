# Question 2
# Develop a class that would represent any bank account that we can open at a bank, and perform basic operations. Use
# the class created above to demonstrate its capabilities.
class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance=0):
        """Initialize a new bank account object."""
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_balance

    def check_deposit (self):
        """Check the deposit of the bank account object."""
        return self.balance

    def save_deposit(self, amount):
        """Add the deposit to the bank account object."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw_deposit (self, amount):
        """Withdraw the deposit from the bank account object."""
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance = self.balance - amount
        return self.balance

bank_account1 = BankAccount("Michael", "0000111122220001", 50000)
bank_account2 = BankAccount("Sean", "0000111222200002", 8000)
print(bank_account1.check_deposit())
print(bank_account1.save_deposit(5000))
print(bank_account1.check_deposit())
print(bank_account2.check_deposit())
print(bank_account2.withdraw_deposit(7850))
print(bank_account2.check_deposit())
print(bank_account2.withdraw_deposit(5000))