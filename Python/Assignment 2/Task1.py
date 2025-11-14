# Task 1: Check if a Number is Even or Odd

# Loop to check multiple numbers
while True:
    # Take integer input from the user
    number = int(input("Enter an integer: "))

    # Check whether the number is even or odd using if-else statement
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
    
    # Ask user if they want to check another number
    choice = input("Do you want to check another number? (yes/no): ").lower()
    if choice != 'yes' and choice != 'y':
        print("Thank you for using the program!")
        break
# End of the program
