# Basic Calculator using Python

print("===================================")
print("       BASIC CALCULATOR")
print("===================================")

# Input two numbers to perform calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display menu of operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (^)")

choice = input("\nEnter your choice (1-6): ")

# Perform calculation by checking the user's choice
if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError! Division by zero is not allowed.")

elif choice == "5":
    if num2 != 0:
        result = num1 % num2
        print(f"\nResult: {num1} % {num2} = {result}")
    else:
        print("\nError! Modulus by zero is not allowed.")

elif choice == "6":
    result = num1 ** num2
    print(f"\nResult: {num1} ^ {num2} = {result}")
# If the user enters an invalid choice
else:
    print("\nInvalid choice! Please select a number between 1 and 6.")
