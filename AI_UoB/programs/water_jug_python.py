LIMIT = 1000
capacityOfJugA = 0
capacityOfJugB = 0

def displayStatus(stepNumber, a, b):
    print(f"{'':18}{stepNumber:<10}{a:<10}{b:<10}")

def findMinimum(val1, val2):
    return min(val1, val2)

def findSolution(req):
    global capacityOfJugA, capacityOfJugB
    a = b = step = temp = 0
    print(f"\n{'':18}{'Step #':<10}{'Jug A':<10}{'Jug B':<10}\n")
    while (b != req) and (step < LIMIT):
        step += 1
        if a == 0:
            a = capacityOfJugA
            print(f"{'Fill A':<20}", end="")
            displayStatus(step, a, b)
        elif b == capacityOfJugB:
            b = 0
            print(f"{'Empty Jug B':<20}", end="")
            displayStatus(step, a, b)
        else:
            temp = findMinimum(capacityOfJugB - b, a)
            a = a - temp
            b = b + temp
            print(f"{'Pour A in B':<20}", end="")
            displayStatus(step, a, b)
    success = 1 if step != LIMIT else 0
    return success, step

if __name__ == "__main__":
    while True:
        capacityOfJugA = int(input("Enter the Capacity of Jug A: "))
        capacityOfJugB = int(input("Enter the Capacity of Jug B: "))
        required = int(input("Water Required to be filled in Jug B: "))
        try:
            if capacityOfJugB < required:
                raise ValueError(f"Error: {required} liter(s) cannot be adjusted in Jug B of {capacityOfJugB} liter(s)")
            elif capacityOfJugA == capacityOfJugB and capacityOfJugB != required:
                raise ValueError("Error! Invalid Input Values")
            else:
                success, steps = findSolution(required)
                if success:
                    print(f"\n\nCalculated Solution Taken in {steps} step(s)\n")
                    print("*" * 45 + "\n")
                else:
                    print(f"\n\nSorry. Unable to calculate result even after {steps} steps\n")
                    print("*" * 45 + "\n")
        except ValueError as e:
            print(e)