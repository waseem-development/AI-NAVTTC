while(True):
    a = int(input("Enter first number: "))
    operator = input("+ or - or x or /: ")
    b = int(input("Enter second number: "))

    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "x" or operator == "*" :
        print(a*b)
    elif operator == "/":
        print(a/b)
    else:
        print("Invalid Operator or character")
