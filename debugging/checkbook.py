#!/usr/bin/python3
"""
checkbook.py

This script simulates a simple checkbook/banking system where a user can
deposit money, withdraw money, and check their account balance.

Usage:
    Run the script and follow the interactive prompts:
        - deposit: Add funds to the checkbook
        - withdraw: Remove funds from the checkbook if sufficient balance
        - balance: Show current balance
        - exit: Quit the program
"""

class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance.

    Attributes:
        balance (float): The current account balance, initialized to 0.0.
    """

    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Args:
            amount (float): The amount of money to deposit.

        Effects:
            Updates the balance and prints the deposited amount and new balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Args:
            amount (float): The amount of money to withdraw.

        Effects:
            - If sufficient funds, deducts amount from balance and prints info.
            - If insufficient funds, prints an error message.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main interactive loop for the checkbook program.

    Prompts the user to:
        - deposit
        - withdraw
        - balance
        - exit

    The loop continues until the user enters 'exit'.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
