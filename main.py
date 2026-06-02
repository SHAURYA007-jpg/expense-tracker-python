import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("\nExpense added successfully!\n")

    except ValueError:
        print("Invalid amount entered.")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.\n")
        return

    print("\n------ Expense List ------")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )

# Total spending
def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spending: ₹{total:.2f}\n")

# Category summary
def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    print("\n------ Category Summary ------")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spending(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
