# Basic Calculator in Python

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input
    choice = input("Enter the number of the operation (1/2/3/4): ")

    # Check for valid operation
    if choice in ['1', '2', '3', '4']:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the operation
        if choice == '1':
            print(f"The result is: {num1 + num2}")
        elif choice == '2':
            print(f"The result is: {num1 - num2}")
        elif choice == '3':
            print(f"The result is: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
    else:
        print("Invalid input. Please select a valid operation.")

# Call the calculator function
calculator()
