from operations.arithmetic_operations import calculate
from print.result_print import text_print


def menu():
    while True:
        try:
            print("\nMenu:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Module (%)")
            print("6. Exit")
            choice = int(input("Enter your choice (1-5): "))

            if choice in (1, 2, 3, 4, 5):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                result = calculate(num1, num2, choice)
                text_print(num1, num2, choice, result)

            elif choice == 6:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Error: enter only numbers")
        except Exception as e:
            return print(e)
