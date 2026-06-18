"""
This module contains a BankAccount class that supports deposits, withdrawals, and transaction history.
"""

class BankAccount:
    """
    A simple BankAccount class to track balance and transaction history.
    """

    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initialize the BankAccount with an owner and an optional initial balance.
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self._add_to_history(f"Account created with balance: {initial_balance}")

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            self._add_to_history(f"Deposited: {amount}")
            print(f"Successfully deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_to_history(f"Withdrew: {amount}")
            print(f"Successfully withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_history(self):
        """
        Return the transaction history as a list of strings.
        """
        return self.transaction_history

    def _add_to_history(self, message):
        """
        Internal method to append a message to the transaction history.
        """
        self.transaction_history.append(message)

if __name__ == "__main__":
    # Demonstration of the BankAccount class
    print("--- BankAccount Demo ---")
    my_account = BankAccount("Alice", 100.0)
    my_account.deposit(50.0)
    my_account.withdraw(30.0)
    my_account.withdraw(200.0)  # Should fail
    
    print("\\nTransaction History:")
    for entry in my_account.get_history():
        print(f"- {entry}")
    
    print(f"\\nFinal Balance: {my_account.balance}")
