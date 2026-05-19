class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(f"Dequeued: {self.queue.pop(0)}")

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("FRONT -> " + " -> ".join(str(x) for x in self.queue) + " -> REAR")

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.display()
    print(f"Peek: {q.peek()}")
    q.dequeue()
    q.display()
    print(f"Empty: {q.isEmpty()}")