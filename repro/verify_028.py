"""
This module provides a BankAccount class to demonstrate basic banking operations
such as depositing, withdrawing, and tracking transaction history.
"""

class BankAccount:
    """
    A simple bank account class.
    
    Attributes:
        balance (float): The current balance of the account.
        history (list): A list of transaction records.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account. Defaults to 0.0.
        """
        self.balance = initial_balance
        self.history = [f"Account created with balance: ${initial_balance:.2f}"]

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        
        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.balance += amount
            record = f"Deposited: ${amount:.2f}"
            self.history.append(record)
            print(record)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are available.
        
        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            record = f"Withdrew: ${amount:.2f}"
            self.history.append(record)
            print(record)
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Returns the transaction history of the account.
        
        Returns:
            list: A list of strings representing the transaction history.
        """
        return self.history

    def get_balance(self):
        """
        Returns the current balance of the account.
        
        Returns:
            float: The current balance.
        """
        return self.balance


if __name__ == "__main__":
    # Demonstration of the BankAccount class
    print("--- BankAccount Demo ---")
    account = BankAccount(100.0)
    
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(150.0)  # Should fail due to insufficient funds
    account.deposit(25.50)
    
    print(f"\nFinal Balance: ${account.get_balance():.2f}")
    print("\nTransaction History:")
    for entry in account.get_history():
        print(f" - {entry}")
