import json
from datetime import datetime

FILE_NAME = "data.json"


# Load data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save data
def save_data(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_data(expenses)
    print("Expense added successfully!")


# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== ALL EXPENSES =====")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Amount: {exp['amount']} | Category: {exp['category']} | Date: {exp['date']}")

    print(f"\nTotal Spent: {calculate_total(expenses)}")


# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        index = int(input("\nEnter expense number to delete: "))
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_data(expenses)
            print(f"Deleted expense: {removed}")
        else:
            print("Invalid number")
    except:
        print("Invalid input")


# Total spending
def calculate_total(expenses):
    return sum(exp["amount"] for exp in expenses)


# Category summary
def category_summary(expenses):
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n===== CATEGORY SUMMARY =====")
    for cat, total in summary.items():
        print(f"{cat}: {total}")


# Menu
def main():
    expenses = load_data()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
