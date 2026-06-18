"""
This module provides a simple BankAccount class to demonstrate basic banking operations
such as depositing, withdrawing, and tracking transaction history.
"""

class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance of the account.
        transaction_history (list): A list of strings recording all transactions.
    """

    def __init__(self, owner, initial_balance=0.0):
        """
        Initializes the BankAccount with an owner and an optional initial balance.

        Args:
            owner (str): The name of the account holder.
            initial_balance (float): The starting balance (default is 0.0).
        """
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = [f"Account created with initial balance: ${initial_balance:.2f}"]

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.balance += amount
            msg = f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
            self.transaction_history.append(msg)
            print(msg)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            msg = f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
            self.transaction_history.append(msg)
            print(msg)

    def display_history(self):
        """
        Prints the transaction history of the account.
        """
        print(f"\nTransaction History for {self.owner}:")
        for transaction in self.transaction_history:
            print(f" - {transaction}")

if __name__ == "__main__":
    # Demonstration of the BankAccount class
    print("--- BankAccount Demo ---")
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(200.0)  # Should fail due to insufficient funds
    account.deposit(10.0)
    
    account.display_history()
    print(f"\nFinal Balance: ${account.balance:.2f}")
