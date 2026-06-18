"""
This module provides a simple BankAccount class for demonstration purposes.
It supports deposits, withdrawals, and tracking transaction history.
"""

class BankAccount:
    """
    A class representing a bank account with basic operations.
    """

    def __init__(self, owner, balance=0.0):
        """
        Initialize the BankAccount with an owner and starting balance.
        """
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
        self._add_to_history("Initial Balance", balance)

    def _add_to_history(self, action, amount):
        """
        Internal method to record transactions.
        """
        self.transaction_history.append({"action": action, "amount": amount, "balance_after": self.balance})

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            self._add_to_history("Deposit", amount)
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account if funds are sufficient.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_to_history("Withdrawal", amount)
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
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
    # Create an account
    account = BankAccount("Alice", 100.0)

    # Perform some transactions
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(150.0)  # Should fail
    account.deposit(20.0)

    # Show history
    print("\nTransaction History:")
    for entry in account.get_history():
        print(f"{entry['action']}: {entry['amount']} | Balance: {entry['balance_after']}")
