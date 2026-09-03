# =========================
# Stack Implementation in Python
# =========================
# Stack: LIFO (Last In, First Out)
# Think of it like a stack of plates:
#   - You can only add/remove from the TOP
#   - [1, 2, 3, 4, 5, 6] => you can only see/access 6
#
# Core Operations:
#   - push  -> add to top
#   - pop   -> remove from top
#   - peek  -> view top without removing
#   - isEmpty -> check if stack is empty
#   - length -> number of elements
#
# We use reverse insertion so index 0 is always the TOP


class Stack:
    def __init__(self):
        self.s = []  # internal list to store stack elements
        # Time: O(1)
        # Space: O(1)

    # ----------------- Length -----------------
    def length(self):
        # Returns number of elements in the stack
        # Time: O(1)
        # Space: O(1)
        return len(self.s)

    # ----------------- isEmpty -----------------
    def isEmpty(self):
        # Returns True if stack is empty, False otherwise
        # Time: O(1)
        # Space: O(1)
        return len(self.s) == 0

    # ----------------- Push -----------------
    def push_func(self, value):
        # Adds a new element to the TOP of the stack (index 0)
        # Time Complexity:
        # Best:  O(1) -> inserting at index 0 in CPython is O(n) internally
        # Avg:   O(n) -> all elements shift right by one
        # Worst: O(n) -> all elements shift right by one
        # Space: O(1)
        self.s.insert(0, value)
        print(f"Pushed {value} | Stack: {self.s}")

    # ----------------- Pop -----------------
    def pop_func(self):
        # Removes and returns the TOP element (index 0)
        # Raises exception if stack is empty
        # Time Complexity:
        # Best:  O(1) -> single element
        # Avg:   O(n) -> all elements shift left by one
        # Worst: O(n) -> all elements shift left by one
        # Space: O(1)
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot pop.")
        popped = self.s.pop(0)
        print(f"Popped {popped} | Stack: {self.s}")
        return popped

    # ----------------- Peek -----------------
    def peek_func(self):
        # Returns the TOP element without removing it
        # Time Complexity:
        # Best/Avg/Worst: O(1)
        # Space: O(1)
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot peek.")
        print(f"Top element: {self.s[0]}")
        return self.s[0]

    # ----------------- Print -----------------
    def print_stack(self):
        # Prints the stack from top to bottom
        # Time: O(n)
        # Space: O(1)
        if self.isEmpty():
            print("Stack is empty")
            return
        print("Stack (top -> bottom):", self.s)


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    stack = Stack()

    # Push elements
    stack.push_func(10)   # Stack: [10]
    stack.push_func(20)   # Stack: [20, 10]
    stack.push_func(30)   # Stack: [30, 20, 10]
    stack.push_func(40)   # Stack: [40, 30, 20, 10]
    stack.print_stack()   # top -> bottom: [40, 30, 20, 10]

    # Peek at top
    stack.peek_func()     # Top element: 40

    # Pop elements
    stack.pop_func()      # Popped 40 | Stack: [30, 20, 10]
    stack.pop_func()      # Popped 30 | Stack: [20, 10]
    stack.print_stack()   # top -> bottom: [20, 10]

    # Length
    print("Length:", stack.length())  # Length: 2

    # isEmpty check
    print("Is empty?", stack.isEmpty())  # Is empty? False

    # Pop remaining
    stack.pop_func()      # Popped 20
    stack.pop_func()      # Popped 10
    stack.print_stack()   # Stack is empty

    # isEmpty after clearing
    print("Is empty?", stack.isEmpty())  # Is empty? True

    # Exception handling
    try:
        stack.pop_func()
    except Exception as e:
        print(f"Error: {e}")  # Error: Stack is empty. Cannot pop.

    try:
        stack.peek_func()
    except Exception as e:
        print(f"Error: {e}")  # Error: Stack is empty. Cannot peek.