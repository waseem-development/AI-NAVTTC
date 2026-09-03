# 🚶 Queue — The FIFO Family

> *"First come, first served. Like a line at a coffee shop, a print job, or a message on WhatsApp."*

---

## 🧠 What Is a Queue?

A **Queue** is a linear data structure that follows one strict rule:

> **FIFO — First In, First Out**

Whatever enters **first** is the **first** to leave. Think of any real line of people — the person who arrived first gets served first.

```
   FRONT                            REAR
     ↓                               ↓
  ┌──────┬──────┬──────┬──────┬──────┐
  │  5   │  15  │  25  │  35  │  45  │
  └──────┴──────┴──────┴──────┴──────┘
     ↑ dequeue                 enqueue ↑
  (exits here)              (enters here)
```

---

## 🎯 Core Operations

| Operation | What It Does | Time |
|-----------|-------------|------|
| `enqueue(val)` | Add element to **REAR** | O(1) |
| `dequeue()` | Remove element from **FRONT** | O(1)* |
| `peek()` | View front element (no remove) | O(1) |
| `isEmpty()` | Check if queue is empty | O(1) |
| `length()` | Count of elements | O(1) |

> *O(n) with Python `list.pop(0)` — use `collections.deque` for true O(1)

---

## 🍕 Real-World Analogies

### 1. Pizza Shop Queue 🍕
Customers line up. First customer gets served first. New customers join the back. Fair and orderly.

### 2. Print Queue 🖨️
5 documents sent to print. They print in the **exact order** you sent them. First in = first out.

### 3. WhatsApp Messages 📱
Messages delivered in the order they were sent. The first message sent is the first one received.

### 4. CPU Task Scheduling ⚙️
OS puts processes in a queue. CPU processes them in order — round robin scheduling is literally a circular queue.

### 5. YouTube Video Buffering 📺
Video chunks buffered in a queue. First chunk buffered = first chunk played. Smooth playback guaranteed.

---

## 🏗️ Types of Queues

---

## 1️⃣ Simple Queue (Regular Queue)

The basic FIFO queue. Insert at rear, delete from front. Nothing fancy.

```
Enqueue →  [ 10 | 20 | 30 | 40 ]  → Dequeue
                                front → 10 leaves first
```

**Problem:** In a fixed-size array, once rear hits the end, you can't reuse freed slots at the front. Memory is wasted. → Solution: Circular Queue.

```python
class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.q.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.q[0]
```

### 🏭 Simple Queue — Production Use & Companies

**Task Queues / Job Queues**
Web servers dump heavy work (image processing, sending emails, generating PDFs) into a simple queue. Worker processes pick them up one by one in order.

| Company | How They Use Simple Queue |
|---------|--------------------------|
| **Shopify** | Order processing queue — orders processed in the sequence received |
| **Stripe** | Payment event queue — charge events processed in strict FIFO order |
| **Twilio** | SMS delivery queue — messages sent in the order queued |
| **SendGrid** | Email delivery queue — bulk emails processed sequentially |
| **GitHub** | CI/CD job queue — builds queued and run in order per repository |

**BFS (Breadth-First Search)**
BFS uses a simple queue to explore graphs level by level — all neighbors at depth 1 first, then depth 2, etc.

| Company | How They Use BFS Queue |
|---------|----------------------|
| **Google** | Web crawler — BFS through hyperlinks to discover pages |
| **Meta** | Friend suggestion — BFS through social graph to find mutual friends |
| **LinkedIn** | "People you may know" — BFS through professional connection graph |
| **Netflix** | Content similarity graph — BFS to find related shows/movies |

---

## 2️⃣ Circular Queue

The smart upgrade. The **last index wraps around** to the first using the `%` (modulo) operator, reusing freed memory slots efficiently.

```
Size = 5
Index:  0     1     2     3     4
      ┌─────┬─────┬─────┬─────┬─────┐
      │  30 │  40 │  50 │  10 │  20 │
      └─────┴─────┴─────┴─────┴─────┘
               ↑                 ↑
             rear              front
      (rear wrapped around to reuse freed slots!)
```

**Key Rules:**
- Empty: `front == rear == -1`
- Full: `(rear + 1) % size == front`
- Enqueue: `rear = (rear + 1) % size`
- Dequeue: `front = (front + 1) % size`

**Why `%` works:**
```
5 % 5 = 0  ← wraps back to start!
6 % 5 = 1
7 % 5 = 2
```

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.cq = [None] * size
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full.")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.cq[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        val = self.cq[self.front]
        self.cq[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val
```

### 🏭 Circular Queue — Production Use & Companies

**CPU Round Robin Scheduling**
The OS cycles through all processes in a fixed time slice. After the last process gets its slice, it wraps back to the first — textbook circular queue.

| Company | How They Use Circular Queue |
|---------|----------------------------|
| **Linux Foundation** | Linux kernel — CFS (Completely Fair Scheduler) uses circular queue concepts |
| **Microsoft** | Windows NT thread scheduler — round robin among equal-priority threads |
| **VMware** | Hypervisor CPU time slicing across virtual machines |
| **Oracle** | JVM garbage collector thread scheduling |

**Audio / Video Streaming Buffers**
A fixed-size circular buffer stores audio/video chunks. Player reads from front, network writes to rear. When buffer is full, oldest chunk is overwritten.

| Company | How They Use Circular Queue |
|---------|----------------------------|
| **Netflix** | Video chunk buffer — circular buffer between network download and video decoder |
| **Spotify** | Audio streaming buffer — circular queue for smooth music playback |
| **Zoom** | Audio jitter buffer — circular queue absorbs network delay variations |
| **YouTube** | Adaptive bitrate buffer — circular queue stores next N seconds of video |

**Network Packet Buffers**
Router NICs (Network Interface Cards) use circular queues. New packets arrive at rear, processed packets leave from front.

| Company | How They Use Circular Queue |
|---------|----------------------------|
| **Cisco** | Router packet queues — circular buffers in network interface hardware |
| **Cloudflare** | DDoS packet processing — circular ring buffers in kernel bypass mode |
| **Amazon** | AWS networking hardware — circular queues in ENI (Elastic Network Interface) |

---

## 3️⃣ DeQueue (Double-Ended Queue)

Insert **and** delete from **both** front AND rear. Maximum flexibility — can behave as both a stack and a queue.

```
insert_at_front → [ 1 | 10 | 20 | 30 | 5 ] ← insert_at_rear
delete_at_front ← [ 1 | 10 | 20 | 30 | 5 ] → delete_at_rear
```

**Real Logic (Array thinking):**
- `insert_at_rear`:  `rear += 1`, `arr[rear] = val`
- `insert_at_front`: `front -= 1`, `arr[front] = val`
- `delete_at_front`: read `arr[front]`, `front += 1`
- `delete_at_rear`:  read `arr[rear]`, `rear -= 1`

```python
class DeQueue:
    def __init__(self):
        self.q = []

    def insert_at_rear(self, value):
        self.q.append(value)        # O(1)

    def insert_at_front(self, value):
        self.q.insert(0, value)     # O(n) with list

    def delete_at_front(self):
        if not self.q: return
        return self.q.pop(0)        # O(n) with list

    def delete_at_rear(self):
        if not self.q: return
        return self.q.pop()         # O(1)
```

### 🏭 DeQueue — Production Use & Companies

**Sliding Window Problems in ML / Data Processing**
The sliding window algorithm (used heavily in ML preprocessing) uses a deque to efficiently track the max/min in a window of data as it slides.

```python
# Max in sliding window of size k — classic deque use
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()       # stores indices
    result = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()                    # remove from rear
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()               # remove from front
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

| Company | How They Use DeQueue |
|---------|---------------------|
| **Google** | Real-time analytics sliding window — max/min across time windows |
| **Meta** | News Feed ranking — sliding window of recent activity scores |
| **Amazon** | Sales trend monitoring — sliding window max/min over time periods |
| **Uber** | Surge pricing algorithm — sliding window of ride requests per area |

**Work Stealing in Parallel Computing**
Each CPU core has its own deque of tasks. When a core finishes its tasks, it "steals" from the **rear** of another core's deque (while the owner takes from its own **front**) — preventing contention.

| Company | How They Use DeQueue |
|---------|---------------------|
| **Intel** | Threading Building Blocks (TBB) — work stealing scheduler |
| **Google** | Go runtime goroutine scheduler — work stealing deque per thread |
| **Oracle** | Java ForkJoinPool — work stealing with deques per worker thread |
| **Microsoft** | .NET ThreadPool — task stealing via deques |

**Palindrome Checking**
Compare characters from both ends simultaneously. Remove from front and rear, check if they match.

| Company | How They Use DeQueue |
|---------|---------------------|
| **Google** | Search autocomplete — palindrome/symmetry detection in query analysis |
| **LeetCode / HackerRank** | Classic algorithm problem used in technical interviews |

**Browser Cache (Forward + Back)**
Browser stores recently visited pages in a deque — insert at front on new visit, delete from rear when cache is full.

| Company | How They Use DeQueue |
|---------|---------------------|
| **Google** | Chrome page cache — deque-based eviction for rendered page cache |
| **Mozilla** | Firefox back/forward cache (bfcache) — deque of cached page states |

---

## 4️⃣ Priority Queue

Elements leave based on **priority**, not arrival order. Internally implemented as a **heap** (not a simple list).

```
Enqueue: patient(priority=3), emergency(priority=1), normal(priority=2)

Dequeue order (lowest number = most urgent):
→ emergency (priority 1)  ← served first regardless of arrival
→ normal    (priority 2)
→ patient   (priority 3)
```

```python
import heapq

pq = []
heapq.heappush(pq, (3, "patient"))
heapq.heappush(pq, (1, "emergency"))
heapq.heappush(pq, (2, "normal"))

print(heapq.heappop(pq))  # (1, 'emergency') ← highest priority first
```

### 🏭 Priority Queue — Production Use & Companies

**Dijkstra's Shortest Path (GPS / Maps)**
The core of every GPS navigation system. Priority queue always expands the node with the lowest cost first.

```python
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]       # (cost, node)
    dist = {start: 0}
    while pq:
        cost, node = heapq.heappop(pq)   # always lowest cost first
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if neighbor not in dist or new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return dist
```

| Company | How They Use Priority Queue |
|---------|----------------------------|
| **Google Maps** | Dijkstra / A* routing — priority queue of road segments by travel time |
| **Uber** | Optimal route calculation for drivers — priority queue of road nodes |
| **Waze** | Real-time rerouting around traffic — A* with priority queue |
| **Apple Maps** | Turn-by-turn navigation — shortest path via priority queue |

**A\* Search in AI / Game Engines**
A* extends Dijkstra with a heuristic. Used in game AI for pathfinding — enemies navigate around obstacles.

| Company | How They Use Priority Queue |
|---------|----------------------------|
| **Unity Technologies** | Unity NavMesh pathfinding — A* with priority queue |
| **Epic Games** | Unreal Engine AI pathfinding for NPCs |
| **Riot Games** | League of Legends champion pathfinding |
| **Valve** | Half-Life / CS:GO bot AI pathfinding |

**OS Process Scheduling**
Higher priority processes (system processes, real-time tasks) must run before lower priority ones. The OS uses a priority queue for this.

| Company | How They Use Priority Queue |
|---------|----------------------------|
| **Linux Foundation** | Linux kernel CFS scheduler — priority queue for process scheduling |
| **Microsoft** | Windows task scheduler — priority-based thread queue |
| **Apple** | macOS Grand Central Dispatch (GCD) — quality-of-service based priority queue |

**Hospital Triage / Emergency Systems**
Patients are served by severity, not arrival time.

| Company | How They Use Priority Queue |
|---------|----------------------------|
| **Epic Systems** | Hospital management software — priority queue for patient triage |
| **GE Healthcare** | ICU monitoring systems — priority alerting queue |

**Event-Driven Simulations**
Simulations process events in chronological order. A priority queue ensures the earliest event is always processed next.

| Company | How They Use Priority Queue |
|---------|----------------------------|
| **Amazon** | AWS event scheduler — events processed by timestamp priority |
| **Google** | Cloud Tasks — delayed job execution via priority queue |
| **Salesforce** | Apex job scheduler — priority-based job execution queue |

---

## 📊 All Queue Types — Quick Comparison

| Type | Insert | Delete | Best For |
|------|--------|--------|----------|
| **Simple Queue** | Rear only | Front only | Task queues, BFS, basic scheduling |
| **Circular Queue** | Rear (wraps) | Front (wraps) | CPU scheduling, audio/video buffers, network packets |
| **DeQueue** | Both ends | Both ends | Sliding window, work stealing, palindrome |
| **Priority Queue** | Any (with priority) | Highest priority first | Pathfinding, OS scheduling, hospital triage |

---

## ⚡ Time & Space Summary

### Simple / Circular Queue
| Operation | Time | Space |
|-----------|------|-------|
| enqueue | O(1) | O(1) |
| dequeue | O(1) | O(1) |
| peek | O(1) | O(1) |

### DeQueue (with `collections.deque`)
| Operation | Time | Space |
|-----------|------|-------|
| insert_at_rear | O(1) | O(1) |
| insert_at_front | O(1) | O(1) |
| delete_at_rear | O(1) | O(1) |
| delete_at_front | O(1) | O(1) |

### Priority Queue (heap-based)
| Operation | Time | Space |
|-----------|------|-------|
| enqueue (heappush) | O(log n) | O(1) |
| dequeue (heappop) | O(log n) | O(1) |
| peek | O(1) | O(1) |

---

## 💡 Python Pro Tip

```python
# For simple queues — use deque, NOT list
from collections import deque

q = deque()
q.append(10)       # enqueue rear  → O(1)
q.appendleft(5)    # enqueue front → O(1)
q.pop()            # dequeue rear  → O(1)
q.popleft()        # dequeue front → O(1)

# list.pop(0) is O(n) — never use it in production queues
```

---

## 🤖 Queues in AI & ML

**DataLoader Prefetch Queue (PyTorch)**
While GPU trains on batch N, background workers prefetch batch N+1 into a queue. Training never waits for data.

```python
from torch.utils.data import DataLoader
# num_workers creates a queue of prefetched batches
loader = DataLoader(dataset, batch_size=32, num_workers=4)
```

**Inference Request Queue**
When you call any AI API, your request joins a queue if servers are busy. Requests are processed in order.

> Used by: OpenAI API, Anthropic API, Google Vertex AI, AWS Bedrock

**BFS for Decision Tree Search**
Game-playing AIs explore all possible moves level by level using BFS + queue before deciding the best move.

> Used by: AlphaGo (Google DeepMind), chess engines, game tree search

---

## 💡 Key Takeaway

> Queues are the **backbone of distributed systems**. Every Amazon order, every WhatsApp message, every YouTube video, every GPS route — somewhere a queue is working silently to make it happen fairly and in order. From simple task scheduling to Kafka powering trillions of events at LinkedIn — the humble queue scales from your textbook to the real world seamlessly.

---

*Master the queue. Master distributed systems.* 🚀
