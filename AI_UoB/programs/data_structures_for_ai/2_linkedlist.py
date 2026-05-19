class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newNode

    def insertAtStart(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertAtPosition(self, index, value):
        if index == 0:
            self.insertAtStart(value)
            return

        newNode = Node(value)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head
        result = "HEAD -> "

        while temp is not None:
            result += str(temp.data) + " -> "
            temp = temp.next

        result += "NULL"
        print(result)

    def readAt(self, index):
        temp = self.head

        for i in range(index):
            temp = temp.next

        return temp.data

    def update(self, index, value):
        temp = self.head

        for i in range(index):
            temp = temp.next

        temp.data = value

    def deleteAt(self, index):
        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        temp.next = temp.next.next


if __name__ == "__main__":
    ll = LinkedList()

    ll.insertAtEnd(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.insertAtEnd(40)
    ll.insertAtEnd(50)

    ll.display()

    ll.insertAtStart(5)
    ll.display()

    ll.insertAtPosition(3, 99)
    ll.display()

    ll.update(3, 77)
    ll.display()

    ll.deleteAt(3)
    ll.display()

    print(ll.readAt(2))