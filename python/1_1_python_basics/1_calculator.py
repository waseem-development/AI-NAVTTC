def calculator():
    while True:
        a = int(input("Enter first number: "))
        operator = input("+ or - or x or /: ")
        b = int(input("Enter second number: "))
        
        if operator == "+":
            print(f"Result: {a + b}")
        elif operator == "-":
            print(f"Result: {a - b}")
        elif operator in ["x", "*"]:
            print(f"Result: {a * b}")
        elif operator == "/":
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid Operator or character")
        
        print("***********************\n")
        
        while True:
            toContinue = input("Do you want to continue? (yes/no): ").lower()
            if toContinue in ["yes", "y"]:
                break
            elif toContinue in ["no", "n"]:
                return
            else:
                print("Please enter either yes or no:")

calculator()