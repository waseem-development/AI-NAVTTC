# =========================
# DeQueue (Double Ended Queue) in Python
# =========================
# Unlike a regular Queue (FIFO), a DeQueue allows:
#   - Insertion from BOTH front and rear
#   - Deletion from BOTH front and rear
#
# Real Logic (Array-based thinking):
#   - front = rear = -1        -> queue is empty
#   - insert_at_rear:  rear += 1, arr[rear] = value
#   - insert_at_front: front -= 1, arr[front] = value  (if front > 0)
#   - delete_at_front: read arr[front], front += 1
#   - delete_at_rear:  read arr[rear],  rear -= 1
#
# Visual:
#   insert_at_front -> [20, 1, 2, 3, 4, 5] <- insert_at_rear
#   delete_at_front <- [20, 1, 2, 3, 4, 5] -> delete_at_rear


class DeQueue:
    def __init__(self):
        self.q = []  # internal list representing our dequeue
        # Time: O(1)
        # Space: O(1)

    # ----------------- isEmpty -----------------
    def isEmpty(self):
        # Real logic: check if front == -1 (nothing inserted yet)
        # Time: O(1)
        # Space: O(1)
        return len(self.q) == 0

    # ----------------- Length -----------------
    def length(self):
        # Real logic: rear - front + 1 gives number of elements
        # Time: O(1)
        # Space: O(1)
        return len(self.q)

    # ----------------- Insert at Rear -----------------
    def insert_at_rear(self, value):
        # Real logic: rear += 1, arr[rear] = value
        # New element goes to the rightmost available slot
        # Time: O(1)
        # Space: O(1)
        self.q.append(value)
        print(f"Inserted at rear: {value} | DeQueue: {self.q}")

    # ----------------- Insert at Front -----------------
    def insert_at_front(self, value):
        # Real logic: front -= 1, arr[front] = value
        # New element goes to the leftmost available slot
        # Only possible if front > 0 (space available at front)
        # Time: O(n) -> all elements shift right to make room at index 0
        # Space: O(1)
        self.q.insert(0, value)
        print(f"Inserted at front: {value} | DeQueue: {self.q}")

    # ----------------- Delete at Front -----------------
    def delete_at_front(self):
        # Real logic: read arr[front], then front += 1
        # Front pointer moves right, effectively removing first element
        # Time: O(n) -> all elements shift left after removal
        # Space: O(1)
        if self.isEmpty():
            print("DeQueue is empty. Cannot delete from front.")
            return
        deleted = self.q.pop(0)
        print(f"Deleted from front: {deleted} | DeQueue: {self.q}")
        return deleted

    # ----------------- Delete at Rear -----------------
    def delete_at_rear(self):
        # Real logic: read arr[rear], then rear -= 1
        # Rear pointer moves left, effectively removing last element
        # Time: O(1) -> just remove last element, no shifting needed
        # Space: O(1)
        if self.isEmpty():
            print("DeQueue is empty. Cannot delete from rear.")
            return
        deleted = self.q.pop()
        print(f"Deleted from rear: {deleted} | DeQueue: {self.q}")
        return deleted

    # ----------------- Peek Front -----------------
    def peek_front(self):
        # Real logic: just read arr[front] without moving the pointer
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            print("DeQueue is empty. Cannot peek.")
            return
        print(f"Front element: {self.q[0]}")
        return self.q[0]

    # ----------------- Peek Rear -----------------
    def peek_rear(self):
        # Real logic: just read arr[rear] without moving the pointer
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            print("DeQueue is empty. Cannot peek.")
            return
        print(f"Rear element: {self.q[-1]}")
        return self.q[-1]

    # ----------------- Print -----------------
    def print_queue(self):
        # Prints all elements from front to rear
        # Time: O(n)
        # Space: O(1)
        if self.isEmpty():
            print("DeQueue is empty")
            return
        print(f"DeQueue (front -> rear): {self.q}")



if __name__ == "__main__":
    q = DeQueue()

    # Insert at rear (like normal queue)
    q.insert_at_rear(10)   # [10]
    q.insert_at_rear(20)   # [10, 20]
    q.insert_at_rear(30)   # [10, 20, 30]
    q.print_queue()        # front -> rear: [10, 20, 30]

    # Insert at front (unique to DeQueue)
    q.insert_at_front(5)   # [5, 10, 20, 30]
    q.insert_at_front(1)   # [1, 5, 10, 20, 30]
    q.print_queue()        # front -> rear: [1, 5, 10, 20, 30]

    # Peek both ends
    q.peek_front()         # Front element: 1
    q.peek_rear()          # Rear element: 30

    # Delete from front
    q.delete_at_front()    # Deleted from front: 1  | [5, 10, 20, 30]
    q.delete_at_front()    # Deleted from front: 5  | [10, 20, 30]
    q.print_queue()        # front -> rear: [10, 20, 30]

    # Delete from rear
    q.delete_at_rear()     # Deleted from rear: 30  | [10, 20]
    q.delete_at_rear()     # Deleted from rear: 20  | [10]
    q.print_queue()        # front -> rear: [10]

    # Length and isEmpty
    print("Length:", q.length())     # Length: 1
    print("Is empty?", q.isEmpty())  # Is empty? False

    # Clear remaining
    q.delete_at_front()    # Deleted from front: 10 | []
    q.print_queue()        # DeQueue is empty

    # Underflow handling
    q.delete_at_front()    # DeQueue is empty. Cannot delete from front.
    q.delete_at_rear()     # DeQueue is empty. Cannot delete from rear.