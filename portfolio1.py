# Portfolio 1: My Daily Allowance Tracker

# **Description:**
# A simple program I made to track my daily allowance and calculate how much cash I have left over after my expenses.

# Enter my allowance and daily spending
my_allowance = input("How much is my allowance for today? ")
my_expenses = input("How much did I spend today? ")

# Convert the strings into decimal numbers so I can do math
my_allowance = float(my_allowance)
my_expenses = float(my_expenses)

# Calculate what I have left
cash_left = my_allowance - my_expenses

# Display my remaining money
print("My remaining cash for today is:", cash_left)
