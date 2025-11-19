#!/usr/bin/env python3
"""
Personal Expenses Tracker
Lab 3 - 
Tracks expenses in Rwandan Francs (RWF) using text files.
"""

import glob
from datetime import datetime

# -------------------------------
# Helper: safely read balance.txt
# -------------------------------
def read_balance():
    """Read balance from balance.txt, return 0 if file missing or empty."""
    try:
        with open("balance.txt", "r") as f:
            content = f.read().strip()
            if content == "":
                return 0
            return int(content)
    except FileNotFoundError:
        return 0

# -------------------------------
# Helper: calculate total expenses
# -------------------------------
def calculate_total_expenses():
    """Sum all expenses across all expense files."""
    total = 0
    for file in glob.glob("expenses_*.txt"):
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    total += int(parts[2])  # amount is 3rd field
    return total

# -------------------------------
# Feature 2: Check Remaining Balance
# -------------------------------
def check_balance():
    initial_balance = read_balance()

    total_expenses = calculate_total_expenses()
    available_balance = initial_balance - total_expenses

    print("\n=== Balance Report ===")
    print(f"Initial/Current Balance: {initial_balance} RWF")
    print(f"Total Expenses to Date: {total_expenses} RWF")
    print(f"Available Balance: {available_balance} RWF")

    # Option to add money
    add_money = input("Do you want to add money? (y/n): ").lower()
    if add_money == "y":
        try:
            amount = int(input("Enter amount to add (RWF): "))
            if amount > 0:
                initial_balance += amount
                with open("balance.txt", "w") as f:
                    f.write(str(initial_balance))
                print(f"New Balance: {initial_balance} RWF")
            else:
                print("Invalid amount. Must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# -------------------------------
# Feature 3: Add New Expense
# -------------------------------
def add_expense():
    initial_balance = read_balance()

    total_expenses = calculate_total_expenses()
    available_balance = initial_balance - total_expenses

    print(f"\nAvailable Balance: {available_balance} RWF")

    date = input("Enter date (YYYY-MM-DD): ")
    item = input("Enter item name: ")

    try:
        amount = int(input("Enter amount (RWF): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print(f"\nDate: {date}\nItem: {item}\nAmount: {amount} RWF")
    confirm = input("Confirm? (y/n): ").lower()

    if confirm == "y":
        if amount > available_balance:
            print("Insufficient balance! Cannot save expense.")
            return

        filename = f"expenses_{date}.txt"

        # Generate sequential ID
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                expense_id = len(lines) + 1
        except FileNotFoundError:
            expense_id = 1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save expense record
        with open(filename, "a") as f:
            f.write(f"{expense_id},{item},{amount},{timestamp}\n")

        print(f"Expense saved! Remaining balance: {available_balance - amount} RWF")

# -------------------------------
# Feature 4: View Expenses
# -------------------------------
def view_expenses():
    print("\n1. Search by item name")
    print("2. Search by amount")
    print("3. Back to main menu")

    choice = input("Enter choice: ")

    if choice == "1":
        keyword = input("Enter item name: ").lower()
        search_expenses(lambda item, amt: keyword in item.lower())
    elif choice == "2":
        try:
            amt = int(input("Enter amount (RWF): "))
            search_expenses(lambda item, amount: amount == amt)
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        return

# Helper: search expenses
def search_expenses(condition):
    for file in glob.glob("expenses_*.txt"):
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 4:
                    expense_id, item, amount, timestamp = parts
                    if condition(item, int(amount)):
                        print(f"{file}: {item} - {amount} RWF at {timestamp}")

# -------------------------------
# Feature 1: Main Menu System
# -------------------------------
def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Check Remaining Balance")
        print("2. View Expenses")
        print("3. Add New Expense")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            print("Saving data... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------------------
# Program Entry Point
# -------------------------------
if __name__ == "__main__":
    main_menu()
