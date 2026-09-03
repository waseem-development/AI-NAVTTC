# 🔗 Linked List — The Dynamic Chain

> *"Unlike arrays, linked lists don't need contiguous memory. Each node knows only one thing: its data, and where the next node lives."*

---

## 🧠 What Is a Linked List?

A **Linked List** is a linear data structure where elements (called **nodes**) are connected via **pointers**. Unlike arrays, elements are **not stored in contiguous memory** — they're scattered in memory, linked together like a chain.

```
Array (contiguous memory):
[ 10 | 20 | 30 | 40 | 50 ]
  0     1    2    3    4   ← fixed indices

Linked List (scattered memory):
[10|→] → [20|→] → [30|→] → [40|→] → [50|✗]
  ↑ each node holds data + pointer to next
```

### Why Not Just Use Arrays?
| Feature | Array | Linked List |
|---------|-------|-------------|
| Insert at start | O(n) — shifts all | O(1) |
| Insert at end | O(1) amortized | O(n) without tail |
| Delete from middle | O(n) — shifts all | O(n) traverse, O(1) delete |
| Random access `arr[i]` | O(1) | O(n) — must traverse |
| Memory | Fixed / contiguous | Dynamic / scattered |
| Cache friendliness | ✅ Excellent | ❌ Poor |

---

## 🏗️ Types of Linked Lists

There are **4 main types**. Each solves a different problem.

---

## 1️⃣ Singly Linked List

The simplest form. Each node has:
- `data` — the value stored
- `next` — pointer to the next node (last node points to `None`)

```
head
  ↓
[10|→] → [20|→] → [30|→] → [40|→] → [50|None]
```

### Node Structure
```python
class Node:
    def __init__(self, info, next=None):
        self.data = info   # value
        self.next = next   # pointer to next node
```

### Core Operations & Complexity

| Operation | Best | Avg | Worst | Space |
|-----------|------|-----|-------|-------|
| insert_at_start | O(1) | O(1) | O(1) | O(1) |
| insert_at_end | O(1)* | O(n) | O(n) | O(1) |
| insert_in_middle | O(1) | O(n) | O(n) | O(1) |
| delete_from_start | O(1) | O(1) | O(1) | O(1) |
| delete_from_end | O(1)* | O(n) | O(n) | O(1) |
| delete_from_middle | O(1) | O(n) | O(n) | O(1) |
| search | O(1) | O(n) | O(n) | O(1) |

> *O(1) when list is empty or single node

### Full Implementation
```python
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t1 = self.head
        while t1.next is not None:
            t1 = t1.next
        t1.next = temp

    def insert_at_start(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_in_middle(self, value, x):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t1 = self.head
        while t1 is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print(f"Value {x} not found")

    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        t1 = self.head
        while t1.next.next is not None:
            t1 = t1.next
        t1.next = None

    def delete_from_middle(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.delete_from_start()
            return
        t1 = self.head
        while t1.next is not None:
            if t1.next.data == value:
                t1.next = t1.next.next
                return
            t1 = t1.next
        print(f"Value {value} not found")

    def print_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head
        while t1 is not None:
            print(f"{t1.data} -> ", end="")
            t1 = t1.next
        print("None")
```

### 🏭 Where Is Singly Linked List Used in Production?

**Hash Table Chaining (Most Common)**
When two keys hash to the same bucket, a singly linked list stores the chain of colliding entries. This is the backbone of Python's `dict` and Java's `HashMap`.

> **Used by:** Python interpreter (dict internals), Java HashMap, Redis hash objects

**Music / Media Playlists**
A playlist where you can only go forward — each song points to the next. Shuffle? Rebuild the list. Can't go back easily.

> **Used by:** Early Spotify playlist implementations, VLC media player internals

**Symbol Tables in Compilers**
Compilers store variable names and their info in symbol tables, often implemented as linked lists within hash buckets.

> **Used by:** GCC, LLVM/Clang, Python's CPython compiler

**Undo History (One Direction)**
Some lightweight editors use a singly linked list for undo — you can only go back, not forward.

> **Used by:** Simple text editors, early versions of Vim

**Memory Allocators (Free List)**
The OS keeps a singly linked list of free memory blocks. `malloc()` in C walks this list to find a free chunk.

> **Used by:** Linux kernel (`kmalloc`), glibc, jemalloc (used by Firefox, Meta)

---

## 2️⃣ Doubly Linked List

Each node has **two pointers** — one to the next node, one to the previous. You can traverse in **both directions**.

```
         head
           ↓
None ← [10|⇄] ↔ [20|⇄] ↔ [30|⇄] ↔ [40|⇄] → None
         prev  next  prev  next  ...
```

### Node Structure
```python
class Node:
    def __init__(self, value, next=None, prev=None):
        self.data = value
        self.next = next   # pointer forward
        self.prev = prev   # pointer backward
```

### Core Operations & Complexity

| Operation | Best | Avg | Worst | Space |
|-----------|------|-----|-------|-------|
| insert_at_start | O(1) | O(1) | O(1) | O(1) |
| insert_at_end | O(1)* | O(n) | O(n) | O(1) |
| insert_in_middle | O(1) | O(n) | O(n) | O(1) |
| delete_from_start | O(1) | O(1) | O(1) | O(1) |
| delete_from_end | O(1) with tail | O(n) | O(n) | O(1) |
| delete_from_middle | O(1) | O(n) | O(n) | O(1) |

> Advantage over singly: delete a node in O(1) if you already have the pointer (no need to find previous node)

### Full Implementation
```python
class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = temp
        temp.prev = t

    def insert_at_start(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_in_middle(self, value, x):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t:
            if t.data == x:
                if t.next is None:
                    t.next = temp
                    temp.prev = t
                else:
                    temp.next = t.next
                    t.next.prev = temp
                    t.next = temp
                    temp.prev = t
                return
            t = t.next
        print(f"Value {x} not found")

    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        t = self.head
        while t.next.next:
            t = t.next
        t.next = None

    def delete_from_middle(self, value):
        if self.head is None:
            print("List is empty")
            return
        t = self.head
        if t.data == value:
            self.head = t.next
            if self.head:
                self.head.prev = None
            return
        while t and t.data != value:
            t = t.next
        if t is None:
            print(f"Value {value} not found")
            return
        if t.prev:
            t.prev.next = t.next
        if t.next:
            t.next.prev = t.prev

    def print_doubly_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        t = self.head
        while t:
            print(f"{t.data} <=> ", end="")
            t = t.next
        print("None")
```

### 🏭 Where Is Doubly Linked List Used in Production?

**Browser History (Back & Forward)**
Pressing Back goes to `prev`, pressing Forward goes to `next`. Both directions need to work instantly — that's a doubly linked list.

> **Used by:** Chrome (Chromium), Firefox, Safari — all implement browser history as a doubly linked list

**LRU Cache (Most Famous Use)**
Least Recently Used cache combines a doubly linked list + hash map. Most recently used items stay at the head, least recently used at the tail. When cache is full, delete from tail in O(1).

```
[Most Recent] ↔ [A] ↔ [B] ↔ [C] ↔ [D] [Least Recent]
```

> **Used by:** Redis (LRU eviction policy), Memcached, CDN caches at Cloudflare, Akamai

**Text Editor Cursor Movement**
Moving cursor left/right in a text editor. Each character/line is a node. `prev` = go left, `next` = go right.

> **Used by:** Vim (gap buffer variant), Emacs, early VS Code internals

**Thread Scheduling in OS**
The Linux kernel uses a doubly linked list to manage the run queue of threads. Threads are added/removed from both ends efficiently.

> **Used by:** Linux kernel (`list_head` — a famous doubly linked list in C), Windows NT thread scheduler

**Music Player with Previous/Next**
Spotify's "now playing" queue where you can go to previous song or next song.

> **Used by:** Spotify, Apple Music, YouTube Music

**Undo/Redo Systems**
Two pointers let you go forward (redo) and backward (undo) through history.

> **Used by:** VS Code, Photoshop, Google Docs, Microsoft Word

---

## 3️⃣ Circular Singly Linked List

Like a singly linked list, but the **last node points back to the head** instead of `None`. It forms a **loop**.

```
head
  ↓
[10|→] → [20|→] → [30|→] → [40|→]
  ↑_________________________________|
  (last node points back to head)
```

### Core Operations & Complexity

| Operation | Best | Avg | Worst | Space |
|-----------|------|-----|-------|-------|
| insert_at_start | O(1)* | O(n) | O(n) | O(1) |
| insert_at_end | O(1)* | O(n) | O(n) | O(1) |
| insert_in_middle | O(1) | O(n) | O(n) | O(1) |
| delete_from_start | O(1)* | O(n) | O(n) | O(1) |
| delete_from_end | O(1)* | O(n) | O(n) | O(1) |

> *O(n) because you must find the last node to update its `next` pointer

### Full Implementation
```python
class CircularSinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head   # points to itself
            return
        t1 = self.head
        while t1.next is not self.head:
            t1 = t1.next
        t1.next = temp
        temp.next = self.head       # wrap back to head

    def insert_at_start(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
            return
        t1 = self.head
        while t1.next is not self.head:
            t1 = t1.next
        temp.next = self.head
        self.head = temp
        t1.next = self.head         # last node → new head

    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is self.head:
            self.head = None
            return
        t1 = self.head
        while t1.next is not self.head:
            t1 = t1.next
        self.head = self.head.next
        t1.next = self.head

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is self.head:
            self.head = None
            return
        t1 = self.head
        while t1.next.next is not self.head:
            t1 = t1.next
        t1.next = self.head

    def print_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head
        while True:
            if t1.next is not self.head:
                print(f"{t1.data} -> ", end="")
            else:
                print(f"{t1.data} -> (back to head: {self.head.data})")
            t1 = t1.next
            if t1 is self.head:
                break
```

### 🏭 Where Is Circular Singly Linked List Used in Production?

**Round Robin CPU Scheduling**
The OS cycles through all processes infinitely. After the last process, it loops back to the first. That's a circular singly linked list being traversed forever.

> **Used by:** Linux kernel process scheduler, Windows task scheduler, embedded RTOS (FreeRTOS)

**Multiplayer Games — Turn Management**
In board games (chess, card games), after the last player's turn, it wraps back to the first player. A circular linked list manages this naturally.

> **Used by:** Chess.com, online card game servers, game engines

**Circular Buffers in Networking**
Network drivers use circular buffers (built on circular linked lists) to handle incoming packets. When the buffer is full, it overwrites the oldest data.

> **Used by:** Linux network drivers, embedded systems, IoT devices

**Media Players — Loop Mode**
When you enable "repeat all" on a playlist, the player loops through songs forever — circular linked list behavior.

> **Used by:** VLC, Spotify (repeat queue), YouTube Music

**Token Ring Networks (Historical)**
The old Token Ring network protocol passed a "token" around all computers in a circle. Only the computer holding the token could transmit. Classic circular linked list.

> **Used by:** IBM Token Ring (historical), some industrial automation networks

---

## 4️⃣ Circular Doubly Linked List

The ultimate linked list. **Two pointers (next + prev)** AND **last node wraps back to head** AND **head's prev points to last node**. Full circle, both directions.

```
         head
           ↓
    ┌──→ [10|⇄] ↔ [20|⇄] ↔ [30|⇄] ↔ [40|⇄] ←──┐
    │      ↑                              |       │
    └──────┘ prev of head = last node     └───────┘
             next of last = head
```

### Core Operations & Complexity

| Operation | Best | Avg | Worst | Space |
|-----------|------|-----|-------|-------|
| insert_at_start | O(1)* | O(n) | O(n) | O(1) |
| insert_at_end | O(1)* | O(n) | O(n) | O(1) |
| insert_in_middle | O(1) | O(n) | O(n) | O(1) |
| delete_from_start | O(1)* | O(n) | O(n) | O(1) |
| delete_from_end | O(1)** | O(n) | O(n) | O(1) |
| delete_from_middle | O(1) | O(n) | O(n) | O(1) |

> *O(n) without tail pointer — O(1) if tail is maintained separately
> **With `head.prev` pointing to last node, delete_from_end can be O(1)!

### Full Implementation
```python
class CircularDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp.prev = self.head
            return
        t = self.head
        while t.next is not self.head:
            t = t.next
        t.next = temp
        temp.prev = t
        temp.next = self.head
        self.head.prev = temp

    def insert_at_start(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp.prev = self.head
            return
        t = self.head
        while t.next is not self.head:
            t = t.next
        temp.next = self.head
        self.head.prev = temp
        t.next = temp
        temp.prev = t
        self.head = temp

    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is self.head:
            self.head = None
            return
        t = self.head
        while t.next is not self.head:
            t = t.next
        self.head = self.head.next
        self.head.prev = t
        t.next = self.head

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is self.head:
            self.head = None
            return
        t = self.head
        while t.next.next is not self.head:
            t = t.next
        t.next = self.head
        self.head.prev = t

    def delete_from_middle(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.delete_from_start()
            return
        t = self.head.next
        while t is not self.head:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        print(f"Value {value} not found")

    def print_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        t = self.head
        while True:
            if t.next is not self.head:
                print(f"{t.data} <=> ", end="")
            else:
                print(f"{t.data} <=> (back to head: {self.head.data})")
            t = t.next
            if t is self.head:
                break
```

### 🏭 Where Is Circular Doubly Linked List Used in Production?

**Advanced LRU Cache**
An upgraded version of doubly linked list LRU. The circular structure makes it even easier to move nodes to the front without checking for None boundaries.

> **Used by:** High-performance cache systems, database buffer pools (PostgreSQL, MySQL InnoDB buffer pool)

**Fibonacci Heap**
Used in Dijkstra's shortest path algorithm (advanced version). Fibonacci heaps internally use circular doubly linked lists to manage heaps of trees efficiently.

> **Used by:** Google Maps routing, GPS navigation systems, network routing protocols (OSPF)

**Window Manager / Desktop Environments**
When you press Alt+Tab to cycle through windows, the window manager cycles through open windows in a circle — forward and backward.

> **Used by:** Linux GNOME/KDE window managers, Windows DWM (Desktop Window Manager)

**Josephus Problem & Game Simulations**
Famous CS problem: N people stand in a circle, every K-th person is eliminated. The circular doubly linked list models this perfectly.

> **Used by:** Simulation engines, competitive programming, game theory models

**OS Thread Ring / Real-Time Systems**
Real-time operating systems that need to cycle through tasks in both directions (priority upgrades going backward, normal scheduling going forward).

> **Used by:** VxWorks (used in Boeing, NASA), QNX (used in cars — BlackBerry), FreeRTOS

---

## 📊 All Types — Quick Comparison

| Type | Direction | Circular | Best For |
|------|-----------|----------|----------|
| **Singly** | Forward only | ❌ | Simple lists, hash chaining, memory allocators |
| **Doubly** | Both ways | ❌ | LRU cache, browser history, undo/redo |
| **Circular Singly** | Forward + loops | ✅ | Round robin scheduling, playlists on repeat |
| **Circular Doubly** | Both + loops | ✅ | Advanced caches, window managers, Fibonacci heaps |

---

## 🤖 Linked Lists in AI & ML

### Dynamic Computation Graphs
PyTorch builds computation graphs dynamically. Each operation node links to the next via pointers — essentially a linked structure for backpropagation.

### Attention Mechanism (Transformer Internals)
The key-value memory in attention layers is accessed sequentially through pointer-like structures, similar to linked list traversal.

### LRU Cache for ML Model Serving
When serving ML models, the inference server caches the most recently used model weights in GPU memory using an LRU cache — built on a doubly linked list + hash map.

> **Used by:** TensorFlow Serving, NVIDIA Triton Inference Server, Hugging Face TGI

### Graph Neural Networks
GNNs represent graph nodes and their neighbors using adjacency lists — each implemented as a linked list of neighbor nodes.

---

## 💡 Key Takeaway

> Linked lists are the **foundation of dynamic data structures**. Every hash map collision chain, every browser history, every LRU cache, every OS scheduler — somewhere underneath, a linked list is quietly doing the heavy lifting. You don't always see them directly in Python (where `list` hides everything), but the moment you touch systems programming, databases, or OS internals — linked lists are everywhere.

---

*Master linked lists. Master memory.* 🧠
