"""
This module provides a BankAccount class to manage deposits, withdrawals, and transaction history.
"""

class BankAccount:
    """
    A class representing a bank account.
    """

    def __init__(self, owner, balance=0.0):
        """
        Initialize the bank account with an owner and an optional starting balance.
        """
        self.owner = owner
        self.balance = balance
        self.history = []
        self._record_transaction("Account Created", balance)

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            self._record_transaction("Deposit", amount)
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are available.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._record_transaction("Withdrawal", amount)
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def _record_transaction(self, type, amount):
        """
        Internal method to record a transaction in the account history.
        """
        self.history.append({
            "type": type,
            "amount": amount,
            "resulting_balance": self.balance
        })

    def get_history(self):
        """
        Return the transaction history.
        """
        return self.history

if __name__ == "__main__":
    # Demo of the BankAccount class
    print("--- Bank Account Demo ---")
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(200.0)  # Should fail
    
    print("\nTransaction History:")
    for tx in account.get_history():
        print(f"{tx['type']}: ${tx['amount']:.2f} | Balance: ${tx['resulting_balance']:.2f}")
