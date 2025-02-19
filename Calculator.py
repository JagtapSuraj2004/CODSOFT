def main():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed!")
                return
        else:
            print("Error: Invalid operation! Use +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == '__main__':
    main()