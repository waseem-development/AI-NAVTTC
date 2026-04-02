names = []

def displayNames():
    if names:
        print("\nNames List:")
        for name in names:
            print(name)
    else:
        print("\nNames list is empty.")
    print()

def addName(name):
    if name.lower() not in (n.lower() for n in names): # this is called the generator expression
        names.append(name) 
        print(f"\n{name} added successfully!")
    else:
        print(f"\n{name} already exists in the list!")
    displayNames()

def removeName(name):
    for n in names:
        if n.lower() == name.lower():
            names.remove(n)
            print(f"\n{n} removed successfully!")
            displayNames()
            return
    print(f"\n{name} not found in the list!")
    displayNames()

def nameListManager():
    while True:
        name = input("Enter your name: ").lower()
        choice = input("""Press: ? 
                       1 to add a name
                       2 to remove a name
                       3 to display all names 
                       4 to exit
                       => """)
        match choice:
            case "1": 
                addName(name)
            case "2":
                removeName(name)
            case "3":
                displayNames()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Wrong Choice! Try again.\n")

nameListManager()