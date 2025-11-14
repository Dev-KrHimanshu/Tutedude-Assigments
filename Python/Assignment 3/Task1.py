# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """
    Calculate the factorial of a number using a loop.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Alternative implementation using recursion
def factorial_recursive(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Main program - Take input from user and calculate factorial
if __name__ == "__main__":
    while True:
        try:
            # Get input from user
            user_input = input("Enter a non-negative integer to calculate its factorial: ")
            number = int(user_input)
            
            # Calculate and display factorial using loop-based approach
            result = factorial(number)
            print(f"\nFactorial of {number} (using loop): {result}")
            
            # Calculate and display factorial using recursive approach
            result_recursive = factorial_recursive(number)
            print(f"Factorial of {number} (using recursion): {result_recursive}")
            
        except ValueError:
            print("Error: Please enter a valid integer!")
        
        # Ask user if they want to calculate another factorial
        another = input("\nDo you want to calculate factorial of another number? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("Thank you for using the Factorial Calculator!")
            break
