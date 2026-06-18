"""
This module provides a BankAccount class to manage deposits, withdrawals, and transaction history.
"""

class BankAccount:
    """
    A class representing a bank account.
    """

    def __init__(self, owner, balance=0.0):
        """
        Initialize the bank account.

        Args:
            owner (str): The name of the account holder.
            balance (float): The initial balance. Defaults to 0.0.
        """
        self.owner = owner
        self.balance = balance
        self.history = []
        self._add_to_history("Initial balance", balance)

    def deposit(self, amount):
        """
        Deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            self._add_to_history("Deposit", amount)
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_to_history("Withdrawal", amount)
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Get the transaction history.

        Returns:
            list: A list of transaction strings.
        """
        return self.history

    def _add_to_history(self, transaction_type, amount):
        """
        Add a transaction to the history.

        Args:
            transaction_type (str): The type of transaction.
            amount (float): The amount involved.
        """
        self.history.append(f"{transaction_type}: {amount}")

if __name__ == "__main__":
    # Demo
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(200.0)  # Should fail
    
    print("\nTransaction History:")
    for record in account.get_history():
        print(record)
    print(f"Final Balance: {account.balance}")
