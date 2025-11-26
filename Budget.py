import os
import json

def load_data():
    """Load salary and expenses from a file, or initialize if file doesn't exist."""
    data_file = 'budget_data.json'
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading data file. Initializing new data.")
    return {"salary": 0.0, "expenses": []}

def save_data(data):
    """Save salary and expenses to a file."""
    with open('budget_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def calculate_balance(salary, expenses):
    """Calculate remaining balance."""
    total_expenses = sum(expense['amount'] for expense in expenses)
    return salary - total_expenses

def main():
    print("=== Monthly Budget Tracker ===")

    # Load existing data
    data = load_data()
    salary = data["salary"]
    expenses = data["expenses"]

    # Get or update salary
    while True:
        try:
            if salary == 0.0:
                salary_input = input("Enter your monthly salary: $")
                salary = float(salary_input)
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
            else:
                update_salary = input(f"Current salary is ${salary:.2f}. Update? (y/n): ").lower()
                if update_salary == 'y':
                    salary_input = input("Enter new monthly salary: $")
                    salary = float(salary_input)
                    if salary < 0:
                        print("Salary cannot be negative.")
                        continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Update data with new salary
    data["salary"] = salary

    # Add new expense
    while True:
        add_expense = input("Add a new expense? (y/n): ").lower()
        if add_expense != 'y':
            break
        try:
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: $"))
            if amount < 0:
                print("Expense amount cannot be negative.")
                continue
            expenses.append({"description": description, "amount": amount})
        except ValueError:
            print("Please enter a valid number for the expense amount.")

    # Update data with new expenses
    data["expenses"] = expenses
    save_data(data)

    # Calculate and display results
    balance = calculate_balance(salary, expenses)
    print("\n=== Budget Summary ===")
    print(f"Monthly Salary: ${salary:.2f}")
    print("Expenses:")
    if expenses:
        for expense in expenses:
            print(f"  - {expense['description']}: ${expense['amount']:.2f}")
    else:
        print("  No expenses recorded.")
    print(f"Total Expenses: ${sum(expense['amount'] for expense in expenses):.2f}")
    print(f"Remaining Balance: ${balance:.2f}")

if __name__ == "__main__":
    main()