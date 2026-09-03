# =========================
# Queue Implementation in Python
# =========================
# Queue: FIFO (First In, First Out)
# Think of it like a line of people:
#   - New people join from the REAR (enqueue)
#   - People leave from the FRONT (dequeue)
#   - [front] 1, 2, 3, 4, 5 [rear]
#
# Key Concepts:
#   - front = rear = -1  -> queue is empty
#   - First insert: front = 0, rear = 0
#   - Each enqueue: rear += 1
#   - Each dequeue: front += 1
#   - Overflow  -> trying to enqueue when full
#   - Underflow -> trying to dequeue when empty
#
# Problem with arrays for stack/queue:
#   - Raw arrays allow insert/delete at ANY index
#   - Queue restricts this: insert only at rear, delete only at front


class Queue:
    def __init__(self):
        self.q = []  # internal list to store queue elements
        # Time: O(1)
        # Space: O(1)

    # ----------------- isEmpty -----------------
    def isEmpty(self):
        # Returns True if queue has no elements
        # Time: O(1)
        # Space: O(1)
        return len(self.q) == 0

    # ----------------- Length -----------------
    def length(self):
        # Returns number of elements in the queue
        # Time: O(1)
        # Space: O(1)
        return len(self.q)

    # ----------------- Enqueue -----------------
    def enqueue(self, value):
        # Adds element to the REAR of the queue
        # Time: O(1)
        # Space: O(1)
        self.q.append(value)
        print(f"Enqueued {value} | Queue: {self.q}")

    # ----------------- Dequeue -----------------
    def dequeue(self):
        # Removes and returns the FRONT element
        # Time Complexity:
        # Best/Avg/Worst: O(n) -> all elements shift left after pop(0)
        # Space: O(1)
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return
        dequeued = self.q.pop(0)
        print(f"Dequeued {dequeued} | Queue: {self.q}")
        return dequeued

    # ----------------- Peek -----------------
    def peek(self):
        # Returns the FRONT element without removing it
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            print("Queue is empty. Cannot peek.")
            return
        print(f"Front element: {self.q[0]}")
        return self.q[0]

    # ----------------- Print -----------------
    def print_queue(self):
        # Prints queue from front to rear
        # Time: O(n)
        # Space: O(1)
        if self.isEmpty():
            print("Queue is empty")
            return
        print(f"Queue (front -> rear): {self.q}")



if __name__ == "__main__":
    q = Queue()

    q.enqueue(5)     # Queue: [5]
    q.enqueue(15)    # Queue: [5, 15]
    q.enqueue(25)    # Queue: [5, 15, 25]
    q.print_queue()  # front -> rear: [5, 15, 25]

    q.peek()         # Front element: 5

    q.dequeue()      # Dequeued 5  | Queue: [15, 25]
    q.dequeue()      # Dequeued 15 | Queue: [25]
    q.print_queue()  # front -> rear: [25]

    print("Length:", q.length())    # Length: 1
    print("Is empty?", q.isEmpty()) # Is empty? False

    q.dequeue()      # Dequeued 25 | Queue: []
    q.print_queue()  # Queue is empty
    q.dequeue()      # Queue is empty. Cannot dequeue.