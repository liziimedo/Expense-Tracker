# Expense-Tracker
This is an interactive expense tracking system. Users can input and monitor their monthly expenses over multiple months, receiving insights into their spending patterns.
Here's a breakdown of its functionality:

Expense Representation:
The Expense class is defined to encapsulate details about an individual expense, including its name, amount, category, and date.
Input Validation:
The get_valid_input function ensures that user inputs are valid, especially when dealing with numerical values.
Expense Tracking:
The main function, track_expenses, guides users through the process of tracking expenses for multiple months. It prompts for the number of months and iterates through each, collecting information on budgets and individual expenses.
Expense Analysis:
The analyze_expenses function provides users with insights into their spending patterns. It identifies the top spending category and categorizes expenses based on their proportion to the budget.
Category-wise Spending:
The script calculates and displays category-wise spending, presenting the percentage of the total expenses attributed to each expense category.
Expense Distribution:
It categorizes expenses into different spending ranges—low, moderate, and high—based on their percentage relative to the budget.
User Interaction:
The script incorporates user-friendly interactions, such as asking for confirmation before including over-budget expenses and allowing users to decide whether to continue tracking expenses for additional months.
Expense Printing:
Detailed information about each expense, including the name, amount, category, and date, is printed for the user's reference.
Expense Analysis Loop:
After tracking expenses for each month, the script provides an option to analyze expenses and offers the choice to add another month if desired.
