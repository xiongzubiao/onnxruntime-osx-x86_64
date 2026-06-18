"""
This module provides a BankAccount class to manage deposits, withdrawals, and transaction history.
"""

class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance of the account.
        transaction_history (list): A list of transaction records.
    """

    def __init__(self, owner, balance=0.0):
        """
        Initializes the BankAccount with an owner and an optional starting balance.

        Args:
            owner (str): The name of the account holder.
            balance (float): The initial balance. Defaults to 0.0.
        """
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
        if balance > 0:
            self.transaction_history.append(f"Initial deposit: ${balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
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
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Returns the transaction history of the account.

        Returns:
            list: A list of transaction records.
        """
        return self.transaction_history


if __name__ == "__main__":
    # Demo of BankAccount class
    print("--- Bank Account Demo ---")
    account = BankAccount("John Doe", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(150.0)  # Should fail
    
    print("\nTransaction History:")
    for entry in account.get_history():
        print(f"- {entry}")
    
    print(f"\nFinal Balance: ${account.balance:.2f}")
