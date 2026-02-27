#  THIS PROGRAM IS INCOMPLETE I NEED TO COMPLETE IT TOMORROW AFTER GETTING A DEEPER REVISION OF DICTIONARIES
def getNumbers(numbersList):
    while True:
        prompt = input('Enter a number or type "stop": ')
        if not prompt:
            print("Youenterd nothing")
            continue
        elif prompt.lower() == "stop":
            print("Quitting...")
            break
        elif prompt.isdigit() or prompt.startswith("-") and prompt[1:].isdigit():
            numbersList.append(int(prompt))
            continue
        else:
            print("Invalid input!!!")
    return numbersList


def analyzeNumbers(numberList):
    # for operation in numberList:
    #     numberList.append({"operation"})

    count = len(numberList)
    sumNum = sum(numberList)
    minimum = min(numberList)
    maximum = max(numberList)
    average = sumNum / count
    oddNumbers = []
    evenNumbers = []
    numberList.sort()
    for num in numberList:
        if num % 2 == 0:
            evenNumbers.append(num)
        else:
            oddNumbers.append(num)
    result = {
        "count": count,
        "sum": sumNum,
        "mininum": minimum,
        "maximum": maximum,
        "evenNumbers": evenNumbers,
        "oddNumbers": oddNumbers,
        "average": average

    }
    return result


def viewNumbers(numberList):
    for num in numberList:
        print(f"{num} ")


numList = []
while True:
    print(
        """
          Press:
          1- To get/add numbers
          2- Analyze numbers
          3- View Formatted data
          4- Exit
          """
    )

    startingMessage = int(input("Enter your option: "))
    if startingMessage == 1:
        getNum = getNumbers(numList)
        print(f"******** Getting Numbers ******** \n{getNum}")
        continue
    elif startingMessage == 2:
        analyzeNumbers(numList)
        print(f"******** Analysing Numbers ********")
        continue
    elif startingMessage == 3:
        viewNum = viewNumbers(numList)
        print(f"******** View Numbers ********\n {viewNum}")
        continue
    elif startingMessage == 4:
        print("Bye bye 👋🏻")
        exit()
    else:
        print("Plaese enter a valid number: ")
        continue
