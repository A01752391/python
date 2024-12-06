# To run: python3 ps1c.py

# Variables for user inputs
initial_deposit = float(input("Enter the initial deposit: "))

# Variables given
cost_of_dream_home = 800000
portion_down_payment = .25
months = 36

# Calculate the down payment 
down_payment = cost_of_dream_home * portion_down_payment 

# Variables for bisection search
epsilon = 100 # Margin of error for savings
steps = 0  # Counter 
low = 0.0 # Inferior limit
high = 1.0 # Superior limit
best_rate = None # Initialize the best rate as none

# Calculate maximum savings in three years
max_savings = initial_deposit * (1 + (high / 12)) ** months

# Check if the initial deposit is enough for the down payment
if initial_deposit >= down_payment - epsilon:
    best_rate = 0.0  # No interest needed if the deposit is sufficient
elif (max_savings < down_payment):
        best_rate = "None"  # Impossible to reach the down payment
else:
    # Find the lowest rate of return based on bisection search
    while low <= high:
        guess = (high + low) / 2.0  # Initial guess for the interest rate
        
        # Calculate current savings using compound interest formula
        current_savings = initial_deposit * (1 + (guess / 12)) ** months

        if abs(current_savings - down_payment) <= epsilon:
            best_rate = guess # If the guess helps to fit in the margin error
            break
        elif current_savings < down_payment:
            low = guess  # Increase rate, if savings are lower
        else:
            high = guess  # Decrease rate, if savings are higher
        
        steps = steps +1 # Number of iterations

# Outputs
if best_rate == "None":
    print("Best savings rate: None")
    print(f"Steps in bisection search: {steps}")
else:
    print(f"Best savings rate: {best_rate}") 
    print(f"Steps in bisection search: {steps}")