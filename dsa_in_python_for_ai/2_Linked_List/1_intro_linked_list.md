# Linked Lists — The Complete Deep Dive —

*"And He is with you wherever you are."* — **Surah Al-Hadid, 57:4**
*(Every node knows where the next one is — nothing is ever truly lost in a chain.)*

</div>

---

## 📌 Table of Contents

1. [What Even Is a Linked List?](#-what-even-is-a-linked-list)
2. [Why Not Just Use an Array?](#-why-not-just-use-an-array)
3. [The Node — Building Block of Everything](#-the-node--building-block-of-everything)
4. [Singly Linked List](#-singly-linked-list)
5. [Doubly Linked List](#-doubly-linked-list)
6. [Circular Linked List](#-circular-linked-list)
7. [Traversal — Moving Through the Chain](#-traversal--moving-through-the-chain)
8. [Common Operations](#-common-operations)
9. [Real-World Use Cases](#-real-world-use-cases)
10. [Time &amp; Space Complexity](#-time--space-complexity)
11. [Quick Comparison Table](#-quick-comparison-table)
12. [Common Mistakes &amp; Gotchas](#-common-mistakes--gotchas)

---

## 🧠 What Even Is a Linked List?

Imagine a  **treasure hunt** . You start at clue #1. Clue #1 doesn't tell you where ALL the clues are — it only tells you where clue #2 is. Clue #2 tells you where clue #3 is. And so on. The last clue says *"you're done"* (which in code is `None`).

That is **exactly** what a Linked List is.

> A Linked List is a chain of **nodes** where each node holds:
>
> 1. **Data** (the actual value — a number, string, object, etc.)
> 2. **A pointer/reference** to the next node in the chain

```
[ data | next ] ──► [ data | next ] ──► [ data | next ] ──► None
  Node 1               Node 2               Node 3 (last)
```

Unlike arrays, the nodes are  **not sitting next to each other in memory** . They can be scattered anywhere. They find each other purely through pointers.

---

## ⚔️ Why Not Just Use an Array?

This is the most important question to ask. Arrays are simpler — so why use Linked Lists at all?

### The Problem with Arrays

When you create an array, your computer reserves a **contiguous (side-by-side) block of memory** for it.

```
Memory:  [100][101][102][103][104][105]
Array:    [ A ][ B ][ C ][ D ][ E ][ F ]
```

This is fine — until you need to **grow** the array. What if the memory slots `[106][107]` are already taken by something else? Your computer has to:

1. Find a new bigger block somewhere else in memory
2. **Copy every single element** over to the new block
3. Delete the old block

That's expensive. And what if you want to **insert** a value in the middle? Every element after it has to  **shift one position right** .

```
Insert X at index 2:
Before: [ A ][ B ][ C ][ D ][ E ]
After:  [ A ][ B ][ X ][ C ][ D ][ E ]
                      ↑ C, D, E all had to move
```

### How Linked Lists Solve This

With a Linked List:

* **No contiguous memory needed.** New nodes can live anywhere in memory.
* **Insertion is O(1).** Just update two pointers — no shifting.
* **No size limit.** Grows as long as RAM exists.

```
Insert X between Node1 and Node2:

Before: [A|next] ──► [B|next] ──► [C|None]
After:  [A|next] ──► [X|next] ──► [B|next] ──► [C|None]
                      ↑ Just added X and updated pointers. Done.
```

### The Trade-off

Nothing is free. Linked Lists lose one huge array superpower:  **random access** .

With an array: `arr[4]` — instant. O(1).
With a linked list: To get to node #4, you **must walk** from node #1 → #2 → #3 → #4. O(n).

---

## 🧱 The Node — Building Block of Everything

Every linked list is made of nodes. A node is just a tiny container holding two things.

```python
class Node:
    def __init__(self, data):
        self.info = data    # The actual value stored
        self.next = None    # Pointer to the next node (starts as None)
```

When you create a node:

```python
node1 = Node(10)
# node1.info = 10
# node1.next = None   ← points to nothing yet
```

Think of `self.next` as a **sticky note** on the node that says *"the next guy lives at this address in memory."*

> **Why no variable names?**
> You never say `node1`, `node2`, `node3` for a real linked list. That would mean declaring unlimited variables. Instead, you use **one pointer** called `head` that points to the first node, and every node internally points to the next. You reach any node by hopping through the chain.

---

## 🔵 Singly Linked List

The simplest form. Each node only knows about the **next** node. It's a one-way street.

```
head
 │
 ▼
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│  10  │  ●───┼───►│  20  │  ●───┼───►│  30  │ None │
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘
  Node 1              Node 2              Node 3
```

### Building One

```python
class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None   # Empty list — head points to nothing

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link them
n1.next = n2   # Node1 → Node2
n2.next = n3   # Node2 → Node3
# n3.next is already None → end of list

# Assign head
my_list = SinglyLinkedList()
my_list.head = n1
```

Now `my_list.head` points to Node1, Node1 points to Node2, Node2 points to Node3, Node3 points to `None`.

### Key Properties

| Property         | Value                           |
| ---------------- | ------------------------------- |
| Direction        | One-way only (forward)          |
| Can go backward? | ❌ No                           |
| Memory per node  | Low (1 pointer)                 |
| Insert at head   | O(1)                            |
| Insert at tail   | O(n) unless tail pointer stored |
| Search           | O(n)                            |

### Disadvantage

You  **cannot go back** . Once you pass a node, it's gone. If you want to re-visit node 2 after reaching node 3, you have to  **start over from head** .

---

## 🟣 Doubly Linked List

Each node has **two pointers** — one to the next node, one to the **previous** node. You can travel in both directions.

```
        head
         │
         ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ None │ 10 │  ●───┼───►│  ●  │ 20 │  ●───┼───►│  ●  │ 30 │ None │
└──────────────────┘◄───┼───● │    │      │◄───┼───● │    │      │
       Node 1           └──────────────────┘    └──────────────────┘
                               Node 2                  Node 3
```

### The Node

```python
class Node:
    def __init__(self, data):
        self.info = data
        self.next = None   # Points to next node
        self.prev = None   # Points to previous node ← NEW
```

### Why Bother?

* Can traverse **backwards** (useful for undo/redo, browser history)
* Deleting a node is **easier** — you already have a reference to the previous node
* Slightly more memory (extra pointer per node)

### Real Example: Browser History

```
[google.com] ⟺ [youtube.com] ⟺ [github.com] ⟺ [stackoverflow.com]
                                       ▲
                                   you are here

Press Back  → go to youtube.com   (use .prev)
Press Forward → go to stackoverflow.com (use .next)
```

### Key Properties

| Property        | Value                                       |
| --------------- | ------------------------------------------- |
| Direction       | Both ways (forward & backward)              |
| Memory per node | Higher (2 pointers)                         |
| Insert/Delete   | Easier (no need to track prev separately)   |
| Use cases       | Browser history, undo/redo, music playlists |

---

## 🔴 Circular Linked List

The last node does **not** point to `None`. Instead, it points **back to the first node** (head), forming a circle.

```
head
 │
 ▼
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│  10  │  ●───┼───►│  20  │  ●───┼───►│  30  │  ●───┼──┐
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘  │
  ▲                                                     │
  └─────────────────────────────────────────────────────┘
                    Loops back to Node 1!
```

### When Is This Useful?

Think of anything that  **loops infinitely** :

* 🎮 **Multiplayer games** — Player 1 → Player 2 → Player 3 → back to Player 1 (taking turns)
* 🎵 **Music player on repeat** — Song 1 → Song 2 → Song 3 → Song 1 again
* ⚙️ **CPU task scheduling** — Round-robin: Task A → Task B → Task C → Task A
* 🖥️ **Carousel/slider** — Slide 1 → 2 → 3 → back to 1

### Danger Zone ⚠️

Because there's no `None`, a `while temp != None` loop will run  **forever** . You need a different stop condition:

```python
# WRONG for circular — infinite loop!
while temp != None:
    print(temp.info)
    temp = temp.next

# CORRECT — stop when you get back to head
temp = head
while True:
    print(temp.info)
    temp = temp.next
    if temp == head:   # We've gone full circle
        break
```

---

## 🚶 Traversal — Moving Through the Chain

This is the most fundamental operation. You want to **visit every node** — print values, search, count, etc.

### The Two-Pointer Problem

You have `head` — your permanent bookmark to the first node. You **must never move head** (otherwise you lose the start of your list forever).

So you create a **temporary pointer** called `temp` (or `current`) that starts at `head` and travels forward.

```python
temp = head   # temp and head both point to Node 1
              # but temp is FREE to move, head stays fixed
```

Think of it like a  **train station** :

* `head` is the entrance of the station — it never moves
* `temp` is you — you walk through the platforms one by one

### The Traversal Loop

```python
def traverse(head):
    temp = head                  # Start at the first node

    while temp != None:          # Keep going until we hit the end
        print(temp.info)         # Do something with current node's data
        temp = temp.next         # Move to the next node

# Output for [10 → 20 → 30 → None]:
# 10
# 20
# 30
```

### Step-by-step visualization

```
Initial:  temp = head → [10|●] → [20|●] → [30|None]

Step 1:   temp.info = 10    ✓ print 10
          temp = temp.next  → temp now points to [20|●]

Step 2:   temp.info = 20    ✓ print 20
          temp = temp.next  → temp now points to [30|None]

Step 3:   temp.info = 30    ✓ print 30
          temp = temp.next  → temp now points to None

Step 4:   temp == None      → while loop ends
```

### Accessing Specific Nodes

```python
# Access 2nd node's value
head.next.info           # → 20

# Access 3rd node's value
head.next.next.info      # → 30

# Access 3rd node's next (which is None)
head.next.next.next      # → None
```

This chaining works, but for large lists it's ugly and impractical — that's what the temp loop is for.

---

## ⚙️ Common Operations

### 1. Insert at the Beginning — O(1)

```python
def insert_at_head(head, data):
    new_node = Node(data)    # Create new node
    new_node.next = head     # New node points to old head
    head = new_node          # Head now points to new node
    return head

# Before: head → [10] → [20] → [30] → None
# After:  head → [5] → [10] → [20] → [30] → None
```

### 2. Insert at the End — O(n)

```python
def insert_at_tail(head, data):
    new_node = Node(data)

    if head is None:         # Empty list — new node IS the head
        return new_node

    temp = head
    while temp.next != None: # Walk until the last node
        temp = temp.next

    temp.next = new_node     # Last node now points to new node
    return head
```

### 3. Delete a Node — O(n)

```python
def delete_node(head, target):
    if head is None:
        return None

    if head.info == target:   # If it's the head itself
        return head.next      # New head is the second node

    temp = head
    while temp.next != None:
        if temp.next.info == target:
            temp.next = temp.next.next   # Skip over the target node
            return head
        temp = temp.next

    return head   # Target not found
```

### 4. Search — O(n)

```python
def search(head, target):
    temp = head
    position = 1

    while temp != None:
        if temp.info == target:
            return f"Found {target} at position {position}"
        temp = temp.next
        position += 1

    return f"{target} not found"
```

### 5. Length / Count — O(n)

```python
def length(head):
    count = 0
    temp = head
    while temp != None:
        count += 1
        temp = temp.next
    return count
```

### 6. Reverse a Singly Linked List — O(n)

This is a classic interview question. Three pointers needed.

```python
def reverse(head):
    prev = None
    current = head

    while current != None:
        next_node = current.next   # Save next before overwriting
        current.next = prev        # Reverse the pointer
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    return prev   # prev is now the new head

# Before: [1] → [2] → [3] → None
# After:  [3] → [2] → [1] → None
```

---

## 🌍 Real-World Use Cases

### Where Linked Lists Actually Live

| Application                        | Type Used | Why                                    |
| ---------------------------------- | --------- | -------------------------------------- |
| **Browser back/forward**     | Doubly    | Navigate in both directions            |
| **Undo/Redo (Ctrl+Z)**       | Doubly    | Move back and forward through states   |
| **Music playlist on repeat** | Circular  | Loops infinitely                       |
| **OS process scheduling**    | Circular  | Round-robin CPU time slices            |
| **GPS navigation queue**     | Singly    | Next turn, next turn, next turn        |
| **Photo carousel**           | Circular  | Wraps around after last photo          |
| **Memory allocators**        | Singly    | Track free memory blocks               |
| **Blockchain**               | Singly    | Each block points to the previous hash |
| **Hash table chaining**      | Singly    | Handle collisions in buckets           |
| **Call stack / recursion**   | Singly    | Function calls linked in order         |

### Concrete Python Example: Undo System

```python
class UndoSystem:
    def __init__(self):
        self.history = DoublyLinkedList()

    def type_text(self, text):
        self.history.insert_at_tail(text)
        print(f"Typed: {text}")

    def undo(self):
        last = self.history.remove_tail()
        print(f"Undone: {last}")

editor = UndoSystem()
editor.type_text("Hello")
editor.type_text(" World")
editor.type_text("!!!")
editor.undo()   # Removes "!!!"
editor.undo()   # Removes " World"
```

---

## ⏱️ Time & Space Complexity

### Singly Linked List

| Operation                      | Time Complexity | Why                           |
| ------------------------------ | --------------- | ----------------------------- |
| Access by index                | O(n)            | Must walk from head           |
| Search                         | O(n)            | Must walk from head           |
| Insert at head                 | **O(1)**  | Just update head pointer      |
| Insert at tail                 | O(n)            | Must walk to end first        |
| Insert at tail (with tail ptr) | **O(1)**  | Direct access                 |
| Delete at head                 | **O(1)**  | Just update head pointer      |
| Delete at tail                 | O(n)            | Must find second-to-last node |
| Delete in middle               | O(n)            | Must find the node first      |

### Compared to Array

| Operation                 | Array             | Linked List          |
| ------------------------- | ----------------- | -------------------- |
| Access by index           | **O(1)**✅  | O(n) ❌              |
| Insert at beginning       | O(n) ❌           | **O(1)**✅     |
| Insert at end (no resize) | **O(1)**✅  | O(n) ❌              |
| Delete from middle        | O(n) ❌           | O(n) same            |
| Memory (overhead)         | Low ✅            | Higher (pointers) ❌ |
| Cache performance         | **Great**✅ | Poor ❌              |

---

## 📊 Quick Comparison Table

| Feature              | Singly               | Doubly                     | Circular                         |
| -------------------- | -------------------- | -------------------------- | -------------------------------- |
| Direction            | Forward only         | Both                       | Forward (loops)                  |
| `prev`pointer      | ❌                   | ✅                         | Optional                         |
| Last node points to  | `None`             | `None`                   | `head`                         |
| Memory usage         | Low                  | Medium                     | Low/Medium                       |
| Can reverse traverse | ❌                   | ✅                         | ❌ (unless doubly circular)      |
| Infinite loop risk   | ❌                   | ❌                         | ✅ (need careful loop condition) |
| Best for             | Simple queues/stacks | Undo/redo, browser history | Round-robin, carousels           |

---

## ⚠️ Common Mistakes & Gotchas

### 1. Moving `head` Instead of `temp`

```python
# ❌ WRONG — you lose your list forever
while head != None:
    print(head.info)
    head = head.next   # head is gone now!

# ✅ CORRECT — use temp
temp = head
while temp != None:
    print(temp.info)
    temp = temp.next
```

### 2. Forgetting to Check for `None` Before Accessing `.info`

```python
# ❌ Will crash if list is empty
print(head.info)   # AttributeError: 'NoneType' has no attribute 'info'

# ✅ Always check first
if head is not None:
    print(head.info)
```

### 3. Infinite Loop in Circular Lists

```python
# ❌ WRONG — never ends for circular lists
while temp != None:   # temp never becomes None!
    temp = temp.next

# ✅ CORRECT
temp = head
while True:
    # do something
    temp = temp.next
    if temp == head:
        break
```

### 4. Losing the Next Node During Deletion

```python
# ❌ WRONG — you lose access to temp.next.next
temp.next = None           # oops, temp.next.next is now unreachable
temp.next = temp.next.next # this line can't run now

# ✅ CORRECT — save next before unlinking
next_node = temp.next.next   # save first
temp.next = next_node         # then update
```

### 5. Off-by-One in Traversal

```python
# Stop condition matters:
while temp != None:       # visits ALL nodes including last
while temp.next != None:  # stops AT last node (useful for insert-at-tail)
```

---

<div align="center">
---

*وَفَوْقَ كُلِّ ذِي عِلْمٍ عَلِيمٌ*

**"Above every person of knowledge is one more knowing."** — *Surah Yusuf, 12:76*

*Keep learning. The chain never ends.* 🔗

---

**Made with focus in Quetta, Pakistan 🇵🇰**

</div>
