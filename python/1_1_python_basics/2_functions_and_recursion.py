# def func1():
#     print("Hello World!")

# func1()


# def nameFunc(name):
#     greeting = "Hello " + name + " 👋🏻 "
#     return greeting

# callingMyFunction = nameFunc("Waseem")

# print(callingMyFunction)

# ******* Default Parameters *******
# def nameFunc(name = "user"):
#     greeting = "Hello " + name + " 👋🏻 "
#     return greeting
# callingMyFunction = nameFunc()
# callingMyFunction1 = nameFunc("Waseem")
# print(callingMyFunction)
# print(callingMyFunction1)

# ******** Recursion ********
def factorialFunction(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorialFunction(number -1)
number = int(input("Enter a number to print its factorial: "))
callingFactorialFunction = factorialFunction(number)
print(f"Factorial of {number} is {callingFactorialFunction}.")