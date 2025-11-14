import math

# Ask the user for a number as input
number = float(input("Enter a number: "))

# Calculate square root
square_root = math.sqrt(number)

# Calculate natural logarithm (log base e)
natural_log = math.log(number)

# Calculate sine of the number (in radians)
sine_value = math.sin(number)

# Display the calculated results
print(f"\nResults for {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")
