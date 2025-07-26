while True:
    try:
        x = float(input("please input Number 1: "))
        y = float(input("please input Number 2: "))

        mathmatical_op = input(
            "Which mathematical operation do you want to execute: \n"
            "A. Addition\n"
            "B. Multiplication\n"
            "C. Division\n"
            "D. Subtraction\n"
            "Your choice: ").lower()

        if mathmatical_op == "a":
            print(f"Result of {x} + {y} = {x + y}")
        elif mathmatical_op == "b":
            print(f"Result  of {x} * {y} = {x * y}")
        elif mathmatical_op == "c":
            if y == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result of {x} / {y} = {x / y}")
        elif mathmatical_op == "d":
            print(f"Result  of {x} - {y} = {x - y}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

    Try_again = input("\nDo you want to try again? (y/n): ").lower()
    if Try_again != "y":
        print("Thank you!")
        break
