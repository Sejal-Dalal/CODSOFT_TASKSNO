while True:
    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    n = int(input("How many numbers do you want to use? "))

    num = float(input("Enter number: "))

    if choice == "1":
        result = num

        for i in range(n - 1):
            num = float(input("Enter number: "))
            result = result + num

        print("Result:", result)

    elif choice == "2":
        result = num

        for i in range(n - 1):
            num = float(input("Enter number: "))
            result = result - num

        print("Result:", result)

    elif choice == "3":
        result = num

        for i in range(n - 1):
            num = float(input("Enter number: "))
            result = result * num

        print("Result:", result)

    elif choice == "4":
        result = num

        for i in range(n - 1):
            num = float(input("Enter number: "))

            if num == 0:
                print("Cannot divide by zero.")
                break

            result = result / num
        else:
            print("Result:", result)

    else:
        print("Invalid choice.")