import math

# Function to solve a quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1} and {root2}"
    elif discriminant == 0:
        # One real solution
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        # Complex (imaginary) solutions
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"Complex roots: {real_part} ± {imag_part}i"

# Ask user for coefficients
a = float(input("Enter coefficient A: "))
b = float(input("Enter coefficient B: "))
c = float(input("Enter coefficient C: "))

# Solve and print the result
print(solve_quadratic(a, b, c))
