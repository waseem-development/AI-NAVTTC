def numberAnalyzerMachine(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    oddNumbers = []
    evenNumbers = []
    numbers.sort()
    for num in numbers:
        if num % 2 == 0:
            evenNumbers.append(num)
        else:
            oddNumbers.append(num)
    result = {
        "sum": total,
        "mininum": minimum,
        "maximum": maximum,
        "evenNumbers": evenNumbers,
        "oddNumbers": oddNumbers,
        "average": average

    }
    return result

while True:
    numbers = []
    print("****** Enter 5 number to put into number analyzer ******")
    for i in range(0, 5):
        if i == 0:
            i = int(input(f"Enter {i+1}st number: "))
        elif i == 1:
            i = int(input(f"Enter {i+1}nd number: "))
        elif i == 2:
            i = int(input(f"Enter {i+1}rd number: "))
        else: 
            i = int(input(f"Enter {i+1}rd number: "))
        numbers.append(i)
    print(numberAnalyzerMachine(numbers))
    while True:
        wantToContinue = input("Do u want to continue: ").lower()
        if wantToContinue in ["y", "yes"]:
             break
        elif wantToContinue in ["n", "No"]:
            exit()
        else: 
            print("Please enter valid input (y/yes or n/no)")
            continue
