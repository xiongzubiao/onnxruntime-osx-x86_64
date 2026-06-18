"""
Module for verifying bank account operations.
This module provides a BankAccount class with basic banking features.
"""

class BankAccount:
    """
    A class representing a bank account with deposit, withdrawal, and transaction history.
    """
    def __init__(self, owner, balance=0.0):
        """
        Initialize the BankAccount with an owner and starting balance.
        """
        self.owner = owner
        self.balance = balance
        self.history = [f"Account created for {owner} with balance {balance}"]

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount}. New balance: {self.balance}")
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraw money from the account if funds are sufficient.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}. New balance: {self.balance}")
            return True
        return False

    def get_history(self):
        """
        Return the transaction history.
        """
        return self.history

if __name__ == '__main__':
    # Demonstration of BankAccount functionality
    account = BankAccount("John Doe", 100.0)
    print(f"Initial balance: {account.balance}")
    
    account.deposit(50.0)
    account.withdraw(30.0)
    
    print("\nTransaction History:")
    for transaction in account.get_history():
        print(f"- {transaction}")
    
    print(f"\nFinal balance: {account.balance}")
