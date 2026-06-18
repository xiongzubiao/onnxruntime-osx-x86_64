"""
This module provides a simple BankAccount class to demonstrate basic
banking operations like deposits, withdrawals, and transaction history.
"""

class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current balance of the account.
        transaction_history (list): A list of transaction records.
    """

    def __init__(self, owner, initial_balance=0.0):
        """
        Initializes the BankAccount with an owner and an initial balance.

        Args:
            owner (str): The name of the account owner.
            initial_balance (float): The starting balance (default is 0.0).
        """
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []
        if initial_balance > 0:
            self.transaction_history.append(f"Initial deposit: ${initial_balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Returns the transaction history as a list of strings.
        """
        return self.transaction_history

if __name__ == "__main__":
    # Demo of BankAccount class
    print("--- Bank Account Demo ---")
    my_account = BankAccount("John Doe", 100.0)
    my_account.deposit(50.0)
    my_account.withdraw(30.0)
    my_account.withdraw(150.0)  # Should show insufficient funds
    
    print("\nTransaction History:")
    for transaction in my_account.get_history():
        print(f"- {transaction}")
    
    print(f"\nFinal Balance for {my_account.owner}: ${my_account.balance:.2f}")
