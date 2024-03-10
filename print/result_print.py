def text_print(num1, num2, choice, result):
    if choice == 1:
        text = f"The Sum between {num1} and {num2} is: {result}"
        print(text)
    elif choice == 2:
        text = f"The Subtraction between {num1} and {num2} is: {result}"
        print(text)
    elif choice == 3:
        text = f"The Multiplication between {num1} and {num2} is: {result}"
        print(text)
    elif choice == 4:
        text = f"The Division between {num1} and {num2} is: {result}"
        print(text)
    else:
        text = f"The module between {num1} and {num2} is: {result}"
        print(text)
