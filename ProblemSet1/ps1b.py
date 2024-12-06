# To run: python3 ps1b.py

# Set variables for user inputs
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percentage of salary that you want to save, as decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal: "))

# Set variables for calculations
portion_down_payment = 0.25
amount_saved = 0
number_months = 1 # Initialize counter for months
r = 0.05 # Annual rate

# Calculate de down payment 
down_payment = cost_of_dream_home * portion_down_payment 

# Loop to find the ammount of months to save up for a down payment considering a raise
while (amount_saved < down_payment):
    # Verify if is needed to add the raise of every six months
    if (number_months % 6 == 0):
        yearly_salary = yearly_salary + (yearly_salary * semi_annual_raise)
    
    # Calculations needed to convert to months
    monthly_salary = yearly_salary / 12
    monthly_saved = monthly_salary * portion_saved

    # Calculations needed to determine the number of months
    amount_saved += monthly_saved  # Add monthly savings
    amount_saved += amount_saved * (r / 12)  # Add interest on savings
    number_months += 1 # Count months

# Calculate the number of months
print(f"Number of months: {number_months}")