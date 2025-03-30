# Get user input for years of experience and age
experience = int(input("Enter years of work experience: "))
age = int(input("Enter age of staff: "))

# Determine the Annual Tax Revenue (ATR) based on conditions
if experience > 25 and age >= 55:
    atr = 5600000
elif experience > 20 and age >= 45:
    atr = 4480000
elif experience > 10 and age >= 35:
    atr = 1500000
else:
    atr = 550000

# Display the result
print(f"The Annual Tax Revenue (ATR) for the staff is N{atr:,}")
