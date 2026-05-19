arr = [10, 20, 30, 40, 50]

def insertAtEnd(value):
    arr.append(value)

def insertAtPosition(index, value):
    arr.insert(index, value)

def display():
    print("{" + ", ".join(str(x) for x in arr) + "}")

def readAt(index):
    return arr[index]

def update(index, value):
    arr[index] = value

def deleteAt(index):
    arr.pop(index)

if __name__ == "__main__":
    display()
    insertAtEnd(60)
    display()
    insertAtPosition(2, 99)
    display()
    update(2, 77)
    display()
    deleteAt(2)
    display()
    print(readAt(1))