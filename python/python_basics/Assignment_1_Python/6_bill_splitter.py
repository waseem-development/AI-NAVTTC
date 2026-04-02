def calculateSharePerPerson(total, numberOfPeople):
    share = total / numberOfPeople
    return share
while True: 
    total = int(input("Enter the total amount: "))
    numberOfPeople = int(input("Enter the number of people: "))
    share = calculateSharePerPerson(total, numberOfPeople)
    print(f"Share Person = {share}\n")

    while True: 
        shouldContinue = input("""Do you want to continue? 
        1) Yes
        2) No 
        ==> """).lower()
        if shouldContinue in ["y", "yes"]:
            break
        elif shouldContinue in ["n", "no"]:
            exit()
        else: 
            print("Enter a valid input")
    
    