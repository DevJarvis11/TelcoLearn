def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the result.
    Handles division by zero by returning None and printing an error.
    """
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def main_calculator():
    """
    Main function to run a single simple calculation based on user input.
    The program performs one calculation and then exits.
    """
    print("\n--- Simple Python Calculator ---")

    try:
        # Get the first number (a)
        a = float(input("Enter the first number (a): "))
        
        # Get the second number (b)
        b = float(input("Enter the second number (b): "))
        
        # Get the operation (c)
        operation = input("Enter the operation (+, -, *, /): ").strip()

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return # Exit the function if numbers are invalid

    result = None
    
    # Determine which function to call based on the operation
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:
        print(f"Invalid operation: '{operation}'. Please use +, -, *, or /.")
        return # Exit if operation is invalid

    # Print the result if the calculation was successful
    if result is not None:
        print(f"\nResult: {a} {operation} {b} = {result}\n")
            
# Run the main calculator function when the script is executed
main_calculator()