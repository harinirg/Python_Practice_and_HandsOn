# Addition function
def add(a, b):
    return a + b
# Subtraction function
def subtract(a, b):
    return b-a
# Multiplication function
def multiply(a, b):
    return a * b
# Callback function
def callback(operation, operand1, operand2):
    return operation(operand1, operand2)
# Menu Driven Program
while True:
    print("\n===== Calculator Menu =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice = int(input("Enter your choice: "))
    if choice == 1:
        result = callback(add, num1, num2)
        print("Add:", result)

    elif choice == 2:
        result = callback(subtract, num1, num2)
        print("Subtract:", result)

    elif choice == 3:
        result = callback(multiply, num1, num2)
        print("Multiply:", result)
    elif choice == 4:
        print("Program Exited")
        break
    else:
        print("Invalid Choice")