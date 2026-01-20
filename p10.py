# Lambda functions for arithmetic operations
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Division by zero"

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Invoking lambda based on operator
if op == '+':
    print("Result:", add(num1, num2))
elif op == '-':
    print("Result:", sub(num1, num2))
elif op == '*':
    print("Result:", mul(num1, num2))
elif op == '/':
    print("Result:", div(num1, num2))
else:
    print("Invalid operator")
