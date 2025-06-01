num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = float(num1) + float(num2)
        print(f"The result is {result}")
    case "-":
        result = float(num1) - float(num2)
        print(f"The result is {result}")
    case "*":
        result = float(num1) * float(num2)
        print(f"The result is {result}")
    case "/":
        if float(num2) != 0:
            result = float(num1) / float(num2)
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation.")