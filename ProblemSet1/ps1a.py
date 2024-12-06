# To run: python3 ps1a.py

# Set variables for user inputs
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percentage of salary that you want to save, as decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

# Set variables for calculations
portion_down_payment = 0.25
amount_saved = 0
number_months = 1 # Initialize counter of months
r = 0.05 # Annual rate

# Calculations needed to convert to months
monthly_salary = yearly_salary / 12
monthly_saved = monthly_salary * portion_saved

# Calculate down payment 
down_payment = cost_of_dream_home * portion_down_payment 

# Loop to find the ammount of months to save up for a down payment
while (amount_saved < down_payment):
    amount_saved += monthly_saved  # Add monthly savings
    amount_saved += amount_saved * (r / 12)  # Add interest on savings
    number_months += 1 # Count months

# Calculate the number of months
print(f"Number of months: {number_months}")