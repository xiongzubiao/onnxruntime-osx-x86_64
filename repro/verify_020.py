"""
Module for a simple BankAccount implementation.
This module provides a BankAccount class that supports deposits, withdrawals,
and maintaining a transaction history.
"""

class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance of the account.
        transaction_history (list): A list of strings recording transactions.
    """

    def __init__(self, owner, initial_balance=0.0):
        """
        Initialize the BankAccount with an owner and an optional initial balance.

        Args:
            owner (str): The name of the account holder.
            initial_balance (float): The starting balance (default 0.0).
        """
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = [f"Account created for {owner} with balance: ${initial_balance:.2f}"]

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.balance += amount
            record = f"Deposited: ${amount:.2f}"
            self.transaction_history.append(record)
            print(record)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive and <= balance.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            record = f"Withdrew: ${amount:.2f}"
            self.transaction_history.append(record)
            print(record)
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Return the list of transactions.

        Returns:
            list: The transaction history.
        """
        return self.transaction_history

    def __str__(self):
        """
        Return a string representation of the account status.
        """
        return f"BankAccount(Owner: {self.owner}, Balance: ${self.balance:.2f})"


if __name__ == "__main__":
    # Demonstration of the BankAccount class
    print("--- BankAccount Demo ---")
    my_account = BankAccount("Alice", 100.0)
    print(my_account)

    my_account.deposit(50.0)
    my_account.withdraw(30.0)
    my_account.withdraw(150.0)  # Should fail

    print("\nTransaction History:")
    for entry in my_account.get_history():
        print(f"- {entry}")

    print(f"\nFinal State: {my_account}")
