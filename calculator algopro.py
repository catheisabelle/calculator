operator = input("input an operator (+ - * /): ")
num1 = float(input("input your first number: "))
num2 = float(input("input your second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("invalid operator")
