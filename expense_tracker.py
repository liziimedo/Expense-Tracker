from datetime import datetime

class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
# Defined a class called Expense with an __init__ method 
# (constructor) that initializes instances of the class 
# with attributes like name, amount, category, and date.

def get_valid_input(prompt, input_type=float):
    """Get valid user input with type validation."""
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Defined a function get_valid_input that takes a prompt and an optional input type as arguments. 
# It repeatedly asks the user for input until a valid input.

def track_expenses():
    """Track expenses for multiple months."""
    money_left = 0.0  # Added initialization
    num_months = get_valid_input("How many months do you want to track? (Enter a number): ", int)
# Defined a function track_expenses that handles expense tracking for multiple months. 
# It initializes money_left and prompts the user to input the number of months to track.

    for i in range(num_months):
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #Iterated over each month, getting the current date and time using datetime.now().

        # Ask the user to choose a month
        # convert the input to the corresponding month name
        month_num = get_valid_input(f"Choose a month (1-January, 2-February, ..., 12-December) for Month {i + 1}: ", int)
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = month_names[month_num - 1]

        budget = get_valid_input(f'How much budget for {month}? ')

        # Print the budget for the current month, 
        # adjusting for any remaining money from the previous month.
        if i == 0:
            print(f"Your budget for {month} is ${budget:.2f}")
        else:
            budget += money_left
            print(f"Your budget for {month} is ${budget:.2f}")

        # Initialize variables to track total expenses, 
        # a list for individual expenses, and a dictionary for category-wise expenses.
        total_expenses = 0.0
        expenses = []
        category_expenses = {}

        while True:
            expense_name = input("Enter the name of the expense (or type 'done' to finish): ")
            # Entered a loop to input expenses until the user enters 'done'.

            if expense_name.lower() == 'done':
                break

            expense_amount = get_valid_input("Enter the expense amount: ")
            expense_category = input("Enter the category of the expense: ")

            total_expenses += expense_amount

            # Handle over-budget expenses
            if total_expenses > budget:
                over_budget = total_expenses - budget
                print(f"This expense exceeds the budget. If you include this expense, your current expenses will be ${total_expenses}, and you will exceed your budget by ${over_budget}.")
                continue_confirmation = input("Do you want to include this expense? (yes/no) ")
                if continue_confirmation.lower() != 'yes':
                    break

            # Update category-wise spending
            if expense_category not in category_expenses:
                category_expenses[expense_category] = 0.0
            category_expenses[expense_category] += expense_amount

            expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=current_date)
            expenses.append(expense)
            # Created an instance of the Expense class
            # append it to the list of expenses
        
        # Calculate and display expenses and statistics
        total_expenses = sum(expense.amount for expense in expenses)
        money_left = budget - total_expenses
        num_expenses = len(expenses)
        average_expense = total_expenses / num_expenses if num_expenses > 0 else 0.0

        print("\nAll Expenses:")
        for expense in expenses:
            print(f"{expense.name} (${expense.amount}) - Category: {expense.category} - Date: {expense.date}")

        print("\nCategory-wise Spending:")
        for category, amount in category_expenses.items():
            percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0.0
            print(f"{category}: ${amount} ({percentage:.2f}%)")

        print(f"\nTotal Expenses: ${total_expenses}")
        print(f"Number of Expenses: {num_expenses}")
        print(f"Average Expense: ${average_expense:.2f}")
        print(f"Money left for {month}: ${money_left}")

        # Ask if the user wants to roll over remaining money to the next month
        if i != (num_months -1):
            roll_over = input("Do you want to roll over the remaining money to the next month? (yes/no) ")
            if roll_over.lower() == 'no':
                money_left = 0

        # Expense Analysis
        analyze_expenses(expenses, budget)

        # Ask if the user wants to add another month
        if i < num_months - 1:  
            add_month = input("Do you want to add another month? (yes/no) ")
            if add_month.lower() == "no":
                break

    print("\nThank you for using the expense tracker!")

def analyze_expenses(expenses, budget):
    """Analyze and provide insights into the user's spending patterns."""
    print("\nExpense Analysis:")

    # Top Spending Categories
    top_category = get_top_spending_category(expenses, n=1)
    print("Top Spending Category:")
    for category, amount in top_category:
        print(f"{category}: ${amount}")
    # Spending Distribution 
    distribution = get_spending_distribution(expenses, budget)
    print("\nSpending Distribution:")
    for category, data in distribution.items():
        print(f"{category}: {data['count']} expenses")
        print_expenses(data['expenses'])

def get_spending_distribution(expenses, budget):
    """Get the distribution of expenses based on their amounts relative to the budget."""
    ranges = {
        "Low (< 30%)": {"expenses": [], "count": 0},
        "Moderate (30% - 70%)": {"expenses": [], "count": 0},
        "High (> 70%)": {"expenses": [], "count": 0}
    }

    for expense in expenses:
        expense_percentage = (expense.amount / budget) * 100

        if expense_percentage < 30:
            ranges["Low (< 30%)"]["expenses"].append(expense)
            ranges["Low (< 30%)"]["count"] += 1
        elif 30 <= expense_percentage <= 70:
            ranges["Moderate (30% - 70%)"]["expenses"].append(expense)
            ranges["Moderate (30% - 70%)"]["count"] += 1
        else:
            ranges["High (> 70%)"]["expenses"].append(expense)
            ranges["High (> 70%)"]["count"] += 1

    return ranges

def get_top_spending_category(expenses, n=1):
    """Get the top n spending categories."""
    category_expenses = {}
    for expense in expenses:
        if expense.category not in category_expenses:
            category_expenses[expense.category] = 0.0
        category_expenses[expense.category] += expense.amount

    sorted_categories = sorted(category_expenses.items(), key=lambda x: x[1], reverse=True)
    return sorted_categories[:n]

def print_expenses(expenses):
    """Print details of expenses."""
    for expense in expenses:
        print(f"Category: {expense.category} - {expense.name}")

# Run the expense tracking function
track_expenses()