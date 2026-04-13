# Define Expense Class
class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def display(self):
        print(f"{self.date} | {self.category} | ${self.amount:.2f}")


# List to store Expense objects
expenses = []

print("Welcome to the Expense Tracker Console Application!")

while True:
    print("\nSelect an option:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Calculate Total Expenses")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # CREATE
    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")

        new_expense = Expense(category, amount, date)
        expenses.append(new_expense)

        print("Expense added successfully!")

    # READ
    elif choice == '2':
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nRecorded Expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ", end="")
                expense.display()

    # UPDATE
    elif choice == '3':
        if not expenses:
            print("No expenses to update.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ", end="")
                expense.display()

            index = int(input("Enter expense number to update: ")) - 1

            if 0 <= index < len(expenses):
                expenses[index].category = input("Enter new category: ")
                expenses[index].amount = float(input("Enter new amount: "))
                expenses[index].date = input("Enter new date: ")
                print("Expense updated successfully!")
            else:
                print("Invalid selection.")

    # DELETE
    elif choice == '4':
        if not expenses:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ", end="")
                expense.display()

            index = int(input("Enter expense number to delete: ")) - 1

            if 0 <= index < len(expenses):
                expenses.pop(index)
                print("Expense deleted successfully!")
            else:
                print("Invalid selection.")

    # CALCULATE TOTAL
    elif choice == '5':
        total = sum(expense.amount for expense in expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    # EXIT
    elif choice == '6':
        print("Thank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
