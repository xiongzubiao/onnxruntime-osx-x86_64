"""
Module for verifying bank account operations.
This module provides a BankAccount class with basic transaction capabilities.
"""

class BankAccount:
    """
    A class representing a bank account with deposit, withdrawal, and history features.
    """

    def __init__(self, owner, balance=0):
        """
        Initialize the bank account.

        :param owner: The name of the account holder.
        :param balance: The initial balance (default is 0).
        """
        self.owner = owner
        self.balance = balance
        self.history = []
        self._add_to_history("Initial Balance", balance)

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            self._add_to_history("Deposit", amount)
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: The amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_to_history("Withdrawal", amount)
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Return the transaction history.
        """
        return self.history

    def _add_to_history(self, transaction_type, amount):
        """
        Helper method to log transactions.
        """
        self.history.append({
            "type": transaction_type,
            "amount": amount,
            "resulting_balance": self.balance
        })

if __name__ == "__main__":
    # Demonstration of BankAccount functionality
    print(f"--- BankAccount Demo ---")
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(150)  # Should fail
    
    print("\nTransaction History:")
    for entry in account.get_history():
        print(f"{entry['type']}: ${entry['amount']} (Balance: ${entry['resulting_balance']})")
