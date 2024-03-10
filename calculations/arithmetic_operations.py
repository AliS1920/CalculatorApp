def calculate(num1, num2, operation):
    try:
        if operation == 1:
            return num1 + num2
        elif operation == 2:
            return num1 - num2
        elif operation == 3:
            return num1 * num2
        elif operation == 4:
            return num1 / num2
        elif operation == 5:
            return num1 % num2
        elif operation == 6:
            return pow(num1, num2)
        else:
            raise ValueError("Invalid operation")
    except ZeroDivisionError:
        return print("Division by zero is not allowed")
