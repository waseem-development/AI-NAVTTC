items = []

def viewItems():
    if len(items) == 0:
        print("Shopping List is empty.")
    else:
        print("\nShopping List:")
        for index, item in enumerate(items):
            print(f"{index + 1}.) {item['Item Name']} - Rs.{item['Price']}")
    print()


def addItem():
    newItemName = input("Enter item name: ")
    newItemPrice = int(input("Enter new item price: "))
    newItemId = len(items) + 1

    if newItemName.lower() not in (i["Item Name"].lower() for i in items):
        newItem = {
            "id": newItemId,
            "Item Name": newItemName,
            "Price": newItemPrice,
        }
        items.append(newItem)
        print(f"{newItem['Item Name']} successfully added")
    else:
        print(f"{newItemName} already exists in the list!")

    viewItems()


def removeItem(item):
    if len(items) == 0:
        print("Shopping List is empty. Cannot remove anything")
    else:
        for i in items:
            if i["Item Name"].lower() == item.lower():
                print(f"{i['Item Name']} successfully removed")
                items.remove(i)
                break
        else:
            print("Item not found")

    viewItems()


def miniShoppingList():
    while True:
        userInput = input("""What do u like to do?
        1) Add an Item into the list
        2) Remove an Item from the list
        3) View All Items in the list
        4) Exit
        ==> """)

        match userInput:
            case "1":
                addItem()
            case "2":
                item = input("Enter item name to be removed: ")
                removeItem(item)
            case "3":
                viewItems()
            case "4":
                print("Good Bye 👋🏻")
                exit()
            case _:
                print("Invalid choice, try again.\n")


miniShoppingList()