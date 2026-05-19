class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        print(f"Popped: {self.stack.pop()}")

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        print("TOP")
        for item in reversed(self.stack):
            print(f" {item}")
        print("BOTTOM")

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.display()
    print(f"Peek: {s.peek()}")
    s.pop()
    s.display()
    print(f"Empty: {s.isEmpty()}")