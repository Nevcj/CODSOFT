def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot Divide by Zero")

print("=== Calculator ===")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Exit")

while True:
    try:
        choice = int(input("\nEnter your choice: "))
        
        if choice == 5:
            break

        if choice not in range(1, 5):
            raise ValueError("Invalid Choice")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

        print(f"\nResult: {result}")

    except ValueError as e:
        print(f"Error: {e}")
