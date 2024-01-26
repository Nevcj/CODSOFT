import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.punctuation
    else:
        print("Invalid Input")
        return None

    if length <= 0:
        print("Enter a positive vaue")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")

try:
    length = int(input("\nEnter the length: "))
except ValueError:
    print("Invalid Input")
    exit()

complexity = input("\nEnter the complexity [ Low, Medium, High ]: ").lower()

password = generate_password(length, complexity)
print(f"\nGenerated Password: {password}")