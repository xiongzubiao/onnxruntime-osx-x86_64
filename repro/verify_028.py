"""
Module for verifying bank account operations.
Provides a BankAccount class with deposit, withdrawal, and transaction history features.
"""

class BankAccount:
    """
    A class representing a bank account.
    """
    def __init__(self, owner, initial_balance=0.0):
        """
        Initialize the bank account.
        :param owner: Name of the account holder.
        :param initial_balance: Initial balance of the account.
        """
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = [f"Account created for {owner} with balance {initial_balance}"]

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}. New balance: {self.balance}")
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :param amount: Amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}. New balance: {self.balance}")
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Return the transaction history.
        """
        return self.transaction_history

if __name__ == "__main__":
    # Demonstration
    account = BankAccount("John Doe", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(150.0)  # Should fail
    
    print("\\nTransaction History:")
    for entry in account.get_history():
        print(f"- {entry}")
