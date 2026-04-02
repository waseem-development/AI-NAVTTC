# myList = [21,43,54,33,125,364,6,6,31254,13]

# # for item in myList:
# #     print(item)


# for item in range(0, len(myList)):
#     print(myList[item])
# else:
#     print("done!!!")

# # *********** Or simply ***********

# print("\n")

# for item in range(len(myList)):
#     print(myList[item])
# else:
#     print("done!!!")

# print("\n")

# for i in range(0, 100):
#     pass
#     print(i+1)

# print("\n\n\n")


# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# print("\n\n")

# i = 1
# while i < 11:
#     print(f"{number} x {i} = {number * i}")
#     i+=1

# listOfNames = ["Harry", "Steven", "John", "Sarah"]

# for item in range(len(listOfNames)):
#     if listOfNames[item].startswith('S'):
#         print(f"Helllllooooo {listOfNames[item]}")


# ********* Prime or Not *********

# number = int(input("Enter a number: "))

# if number < 2:
#     print(f"{number} is not a prime number")
# else:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print(f"{number} is not a prime number")
#             break
#     else:
#         print(f"{number} is a prime number")

# ********* First n natural numbers *********
# first_N_NaturalNumbers = int(input("Enter a value for N to print first N natural numbers: "))
# i = 1
# sum = 0
# while i <= first_N_NaturalNumbers:
#     sum += i
#     i += 1
# print(f"Sum of first n natural number = {sum}")

# ********* Factorial *********

# number = int(input("Enter a number to get its factorial: "))
# factorial = 1
# for i in reversed(range(1, number + 1)):
#     factorial *= i
# print(f"Factrorial of this number is: {factorial}")
# n = 5
# for i in range(1, n + 1):
#     stars = 2 * i - 1
#     print('*' * stars)
# Pattern - 1
#    *
#   * *
#  * * * 
# numberOfRows = int(input("Enter the number of rows: "))

# for i in range (1, numberOfRows + 1):
#     for j in range(numberOfRows - i):
#         print(" ", end="")
#     for k in range (1, 2*i):
#         print("*", end="")
#     print()


# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits, start=0):
#         print(index, fruit)

number = int(input("Enter a number to get its factorial: "))
for i in reversed(range(1, 11)):
    print(f"{number} x {i} = {number * i}")