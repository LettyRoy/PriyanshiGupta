import math

def calculator():
    print("\nAdvanced Calculator")
    print("1. Power (x^y)")
    print("2. Square Root (√x)")
    print("3. Sine (sin x)")
    print("4. Cosine (cos x)")
    print("5. Tangent (tan x)")
    print("6. Addition (x + y)")
    print("7. Subtraction (x - y)")
    print("8. Multiplication (x * y)")
    print("9. Division (x / y)")
    
    choice = input("Enter your choice (1-9): ")
    
    if choice == '1':
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))
        print("Result: ", math.pow(x, y))
    elif choice == '2':
        x = float(input("Enter a number: "))
        print("Result: ", math.sqrt(x))
    elif choice == '3':
        x = float(input("Enter angle in degrees: "))
        print("Result: ", math.sin(math.radians(x)))
    elif choice == '4':
        x = float(input("Enter angle in degrees: "))
        print("Result: ", math.cos(math.radians(x)))
    elif choice == '5':
        x = float(input("Enter angle in degrees: "))
        print("Result: ", math.tan(math.radians(x)))
    elif choice == '6':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result: ", x + y)
    elif choice == '7':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result: ", x - y)
    elif choice == '8':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result: ", x * y)
    elif choice == '9':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if y != 0:
            print("Result: ", x / y)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid option.")


calculator()
