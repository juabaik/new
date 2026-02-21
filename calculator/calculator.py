#!/usr/bin/env python3
"""
Simple Calculator Application
A basic calculator that supports addition, subtraction, multiplication, and division.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Get a valid operation from user input."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operations[operation], operation
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

def main():
    """Main calculator function."""
    print("=== Simple Calculator ===")
    print("Enter 'q' to quit")
    
    while True:
        try:
            # Get first number
            num1 = get_number("Enter first number: ")
            
            # Get operation
            operation_func, operation_symbol = get_operation()
            
            # Get second number
            num2 = get_number("Enter second number: ")
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Display result
            print(f"\n{num1} {operation_symbol} {num2} = {result}")
            print("-" * 20)
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()