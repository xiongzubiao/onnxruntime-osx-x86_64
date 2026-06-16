"""
Bank Account Management System

This module provides a BankAccount class to manage financial transactions,
including deposits, withdrawals, and transaction history tracking.
"""

import datetime
from typing import List, Dict, Union

class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance of the account.
        history (List[Dict[str, Union[str, float, datetime.datetime]]]): 
            A list of transaction records.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        """
        Initializes the BankAccount with an owner and an optional initial balance.

        Args:
            owner (str): The name of the account holder.
            initial_balance (float): The starting balance (default 0.0).
        """
        self.owner = owner
        self.balance = initial_balance
        self.history = []
        self._add_to_history("Initial Deposit", initial_balance)

    def _add_to_history(self, transaction_type: str, amount: float):
        """
        Records a transaction in the account history.

        Args:
            transaction_type (str): The type of transaction (e.g., 'Deposit').
            amount (float): The amount involved in the transaction.
        """
        record = {
            "timestamp": datetime.datetime.now(),
            "type": transaction_type,
            "amount": amount,
            "resulting_balance": self.balance
        }
        self.history.append(record)

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        self._add_to_history("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account if funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print(f"Insufficient funds for withdrawal of ${amount:.2f}. Current balance: ${self.balance:.2f}")
            return

        self.balance -= amount
        self._add_to_history("Withdrawal", -amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_history(self):
        """
        Prints the transaction history of the account.
        """
        print(f"\nTransaction History for {self.owner}:")
        print("-" * 50)
        for entry in self.history:
            timestamp = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} | {entry['type']:<15} | Amount: {entry['amount']:>10.2f} | Balance: {entry['resulting_balance']:>10.2f}")
        print("-" * 50)

if __name__ == "__main__":
    # Demonstration of BankAccount functionality
    print("--- Bank Account Demo ---")
    my_account = BankAccount("Alice", 1000.0)
    
    my_account.deposit(500.0)
    my_account.withdraw(200.0)
    my_account.withdraw(1500.0) # Should fail due to insufficient funds
    my_account.deposit(100.0)
    my_account.withdraw(300.0)
    
    my_account.get_history()
