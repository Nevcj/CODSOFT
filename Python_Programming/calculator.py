def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot Divide by Zero"
    return x / y

print("=== Calculator ===")

while True:
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid Input")
        continue

     
    print("\n1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input")
        continue

    if choice == 5:
        break

    if choice not in range(1, 5):
        print("Invalid Choice")
        continue

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "Division"

    print(f"\nResult of {operation}: {result}")
