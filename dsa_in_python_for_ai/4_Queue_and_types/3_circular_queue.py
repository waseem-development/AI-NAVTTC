# =========================
# Circular Queue in Python
# =========================
#
# Real Logic (Array-based thinking):
# Normal queue problem: once rear reaches end, we can't reuse
# freed spaces at the front. Circular queue fixes this!
#
# Visual (size = 5):
#
#        0     1     2     3     4
#      +-----+-----+-----+-----+-----+
#      |  10 |  20 |  30 |  40 |  50 |
#      +-----+-----+-----+-----+-----+
#         ^                       ^
#       front                   rear
#
# After dequeue (front moves right):
#      +-----+-----+-----+-----+-----+
#      | free|  20 |  30 |  40 |  50 |
#      +-----+-----+-----+-----+-----+
#               ^                 ^
#             front              rear
#
# After enqueue (rear wraps around using % operator):
#      +-----+-----+-----+-----+-----+
#      |  60 |  20 |  30 |  40 |  50 |
#      +-----+-----+-----+-----+-----+
#         ^    ^
#        rear front
#
# Key Rules:
#   - Empty:    front == rear == -1
#   - Full:     (rear + 1) % size == front
#   - Enqueue:  rear = (rear + 1) % size
#   - Dequeue:  front = (front + 1) % size
#   - One item: front == rear (both at same index)
#
# Why modulo?
#   rear goes: 0, 1, 2, 3, 4, 0, 1, 2 ... (wraps around!)
#   6 % 5 = 1, 7 % 5 = 2, 10 % 5 = 0


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.cq = [None] * size  # fixed-size array
        self.front = -1          # points to front element
        self.rear = -1           # points to rear element
        # Time: O(1)
        # Space: O(n) -> array of given size

    # ----------------- isEmpty -----------------
    def isEmpty(self):
        # Real logic: front == -1 means nothing was ever inserted
        # Time: O(1)
        # Space: O(1)
        return self.front == -1

    # ----------------- isFull -----------------
    def isFull(self):
        # Real logic: if rear+1 wraps around and hits front, no space left
        # (rear + 1) % size == front  means full circle completed
        # Time: O(1)
        # Space: O(1)
        return (self.rear + 1) % self.size == self.front

    # ----------------- Length -----------------
    def length(self):
        # Real logic: calculate number of elements using front and rear
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        # wrapped around case
        return self.size - self.front + self.rear + 1

    # ----------------- Enqueue -----------------
    def enqueue(self, value):
        # Real logic:
        #   if full: stop (overflow)
        #   if first element: front = rear = 0
        #   else: rear = (rear + 1) % size  -> wraps around!
        # Time: O(1)
        # Space: O(1)
        if self.isFull():
            print("Circular Queue is full. Cannot enqueue.")
            return
        elif self.isEmpty():
            # First element: both pointers start at 0
            self.front = self.rear = 0
        else:
            # Move rear forward, wrap around using modulo
            self.rear = (self.rear + 1) % self.size
        self.cq[self.rear] = value
        print(f"Enqueued {value} | Queue: {self.cq} | front={self.front} rear={self.rear}")

    # ----------------- Dequeue -----------------
    def dequeue(self):
        # Real logic:
        #   if empty: stop (underflow)
        #   if one element: reset front = rear = -1
        #   else: front = (front + 1) % size  -> wraps around!
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            print("Circular Queue is empty. Cannot dequeue.")
            return
        deleted = self.cq[self.front]
        self.cq[self.front] = None  # clear the slot
        if self.front == self.rear:
            # Last element removed: reset queue
            self.front = self.rear = -1
        else:
            # Move front forward, wrap around using modulo
            self.front = (self.front + 1) % self.size
        print(f"Dequeued {deleted} | Queue: {self.cq} | front={self.front} rear={self.rear}")
        return deleted

    # ----------------- Peek -----------------
    def peek(self):
        # Real logic: just read arr[front] without moving the pointer
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            print("Circular Queue is empty. Cannot peek.")
            return
        print(f"Front element: {self.cq[self.front]}")
        return self.cq[self.front]

    # ----------------- Print -----------------
    def print_queue(self):
        # Traverse from front to rear using modulo to wrap around
        # Time: O(n)
        # Space: O(1)
        if self.isEmpty():
            print("Circular Queue is empty")
            return
        print("Queue (front -> rear): ", end="")
        i = self.front
        while True:
            print(self.cq[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size  # wrap around
        print()


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    q = CircularQueue(5)  # fixed size of 5

    q.enqueue(10)    # [10,   None, None, None, None]
    q.enqueue(20)    # [10,   20,   None, None, None]
    q.enqueue(30)    # [10,   20,   30,   None, None]
    q.enqueue(40)    # [10,   20,   30,   40,   None]
    q.enqueue(50)    # [10,   20,   30,   40,   50  ]
    q.print_queue()  # 10 20 30 40 50

    q.enqueue(60)    # Full! Cannot enqueue.

    q.peek()         # Front element: 10

    q.dequeue()      # Dequeued 10 | [None, 20, 30, 40, 50]
    q.dequeue()      # Dequeued 20 | [None, None, 30, 40, 50]
    q.print_queue()  # 30 40 50

    # Now rear wraps around to reuse freed slots
    q.enqueue(60)    # [60,   None, 30, 40, 50]
    q.enqueue(70)    # [60,   70,   30, 40, 50]
    q.print_queue()  # 30 40 50 60 70

    print("Length:", q.length())     # Length: 5
    print("Is full?", q.isFull())    # Is full? True
    print("Is empty?", q.isEmpty())  # Is empty? False

    q.dequeue()      # Dequeued 30
    q.dequeue()      # Dequeued 40
    q.dequeue()      # Dequeued 50
    q.dequeue()      # Dequeued 60
    q.dequeue()      # Dequeued 70
    q.print_queue()  # Circular Queue is empty
    q.dequeue()      # Circular Queue is empty. Cannot dequeue.