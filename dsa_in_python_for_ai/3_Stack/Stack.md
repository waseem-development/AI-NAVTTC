# 📚 Stack — The LIFO Master

> *"Last one in, first one out. Like a stack of plates, a pile of books, or your browser's back button."*

---

## 🧠 What Even Is a Stack?

A **Stack** is a linear data structure that follows one strict rule:

> **LIFO — Last In, First Out**

Whatever you put in **last** is the **first** thing to come out. Think of it like a stack of plates at a buffet — you always grab from the **top**, and new plates are always added to the **top**.

```
        TOP
        ↓
    ┌─────────┐
    │   40    │  ← most recently added (you see this)
    ├─────────┤
    │   30    │
    ├─────────┤
    │   20    │
    ├─────────┤
    │   10    │  ← first added (buried at the bottom)
    └─────────┘
```

You **cannot** access 10, 20, or 30 directly. You must pop 40 first.

---

## 🎯 Core Operations

| Operation | What It Does | Time Complexity |
|-----------|-------------|-----------------|
| `push(val)` | Add element to **TOP** | O(1) |
| `pop()` | Remove element from **TOP** | O(1) |
| `peek()` | **View** top element (no remove) | O(1) |
| `isEmpty()` | Check if stack has no elements | O(1) |
| `length()` | Count of elements | O(1) |

---

## 🍽️ Real-World Analogies

### 1. Stack of Plates 🍽️
At a buffet, plates are stacked. You always take the **top** plate. New clean plates go on **top**. Nobody digs to the bottom — that's a stack.

### 2. Browser Back Button 🌐
Every page you visit gets **pushed** onto a stack. When you press **Back**, the current page gets **popped** and you return to the previous one.

```
Visit Google    → Stack: [Google]
Visit YouTube   → Stack: [Google, YouTube]
Visit Reddit    → Stack: [Google, YouTube, Reddit]
Press Back      → Stack: [Google, YouTube]  ← Reddit popped
Press Back      → Stack: [Google]           ← YouTube popped
```

### 3. Undo in Editors ✏️
Every action you perform is pushed. Pressing **Ctrl+Z** pops the last action and undoes it.

### 4. Call Stack in Programming 📞
When a function calls another function, the current function is pushed onto the call stack.

```
main() calls foo()
foo() calls bar()

Stack:
┌─────────┐
│  bar()  │  ← currently running
├─────────┤
│  foo()  │
├─────────┤
│  main() │
└─────────┘

bar() finishes → popped → back to foo()
foo() finishes → popped → back to main()
```

---

## 🐍 Python Implementation

```python
class Stack:
    def __init__(self):
        self.s = []

    def isEmpty(self):
        return len(self.s) == 0

    def length(self):
        return len(self.s)

    def push_func(self, value):
        self.s.insert(0, value)   # index 0 = TOP
        print(f"Pushed {value} | Stack: {self.s}")

    def pop_func(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot pop.")
        popped = self.s.pop(0)
        print(f"Popped {popped} | Stack: {self.s}")
        return popped

    def peek_func(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot peek.")
        print(f"Top element: {self.s[0]}")
        return self.s[0]

    def print_stack(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        print("Stack (top → bottom):", self.s)
```

---

## 🏭 Where Is Stack Used? (By Use Case + Company)

---

### 🔵 1. Call Stack — Function Execution

Every time a function calls another function, the current state (local variables, return address) is **pushed** onto the call stack. When it finishes, it's **popped** and execution returns to the caller.

```
def main():
    foo()
def foo():
    bar()
def bar():
    print("hello")   # ← currently here

Call Stack:
[ bar() ]  ← top (currently running)
[ foo() ]
[ main() ]
```

| Company | How They Use It |
|---------|----------------|
| **Google** | V8 JavaScript engine (Chrome) manages execution entirely via call stack |
| **Meta** | PyPy JIT compiler call stack for Python services |
| **Microsoft** | .NET CLR manages C# / F# call stack for all managed code |
| **Apple** | Swift runtime — every iOS app ever built uses this |
| **Amazon** | AWS Lambda — each function invocation has its own isolated call stack |

---

### 🔵 2. Expression Parsing & Evaluation

Compilers parse math like `3 + (4 * 2)` using a stack. Every `(` is pushed, every `)` triggers a pop and evaluation. This is called the **Shunting-yard algorithm**.

```
Expression: 3 + (4 * 2)
Push 3    → [3]
Push +    → [3, +]
Push (    → [3, +, (]
Push 4    → [3, +, (, 4]
Push *    → [3, +, (, 4, *]
Push 2    → [3, +, (, 4, *, 2]
Hit )     → evaluate 4*2=8 → [3, +, 8]
End       → evaluate 3+8=11 ✓
```

| Company | How They Use It |
|---------|----------------|
| **Google** | Google Sheets formula evaluation engine |
| **Microsoft** | Excel formula parser — used by ~1 billion people |
| **JetBrains** | PyCharm, IntelliJ — real-time code analysis and syntax parsing |
| **MongoDB** | Aggregation pipeline query expression parser |
| **Wolfram** | Mathematica — expression tree evaluation |

---

### 🔵 3. Undo / Redo Systems

Two stacks: one for **undo**, one for **redo**. Every action is pushed onto the undo stack. Ctrl+Z pops from undo and pushes to redo. Ctrl+Y pops from redo back to undo.

```
Type "Hello":   undo=[H, e, l, l, o]   redo=[]
Ctrl+Z x2:      undo=[H, e, l]         redo=[o, l]
Ctrl+Y x1:      undo=[H, e, l, l]      redo=[o]
```

| Company | How They Use It |
|---------|----------------|
| **Microsoft** | Word, Excel, PowerPoint — every Office app, stack-based undo |
| **Adobe** | Photoshop supports up to 1000 undo states — a deep stack |
| **Google** | Google Docs — each collaborator has their own undo stack |
| **Figma** | Every design operation (move, resize, recolor) pushed to a stack |
| **Atlassian** | Confluence and Jira editors — content editing undo history |

---

### 🔵 4. Browser Navigation History

Every page visit is pushed. Back button pops from back-stack and pushes to forward-stack. Visiting a new page clears the forward-stack.

```
Visit A → back=[A]        forward=[]
Visit B → back=[A,B]      forward=[]
Back    → back=[A]        forward=[B]
Visit C → back=[A,C]      forward=[]  ← forward cleared!
```

| Company | How They Use It |
|---------|----------------|
| **Google** | Chrome — each tab has its own back/forward stack |
| **Mozilla** | Firefox session history — stack per tab, persisted across restarts |
| **Apple** | Safari on iOS/macOS — back/forward navigation stack |
| **Microsoft** | Edge browser navigation |

---

### 🔵 5. Syntax Validation (Bracket Matching)

Check if `{[()]}` is valid. Push every opening bracket. When a closing bracket appears, pop and check if they match.

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
```

| Company | How They Use It |
|---------|----------------|
| **JetBrains** | All IDEs — real-time bracket matching as you type |
| **GitHub** | Code diff viewer and syntax highlighting |
| **Google** | Cloud Shell editor, Google Colab notebook |
| **Atlassian** | Bitbucket code viewer |

---

### 🔵 6. Depth-First Search (DFS) — AI & Graph Algorithms

DFS explores as deep as possible before backtracking. Naturally LIFO — push neighbors, pop the deepest one next.

```python
def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()       # LIFO — always go deepest first
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    return visited
```

| Company | How They Use It |
|---------|----------------|
| **Google** | Web crawler — DFS for following links and indexing pages |
| **Meta** | Social graph traversal for friend-of-friend suggestions |
| **LinkedIn** | "Degrees of connection" — DFS through professional network |
| **Netflix** | Content graph traversal for recommendation engine |
| **Uber** | Map graph edge-case traversal for routing |

---

### 🔵 7. Stack Memory (Hardware Level)

Your computer has a dedicated **stack segment** in RAM per thread. Local variables, parameters, and return addresses all live here. The CPU manages it using a **stack pointer register** (RSP on x86-64).

| Company | How They Use It |
|---------|----------------|
| **Intel / AMD** | RSP register — hardware stack pointer in every CPU |
| **ARM** | Mobile chips (every iPhone and Android device) — SP register |
| **Apple** | Every iOS app thread gets 512KB–8MB of stack memory |
| **Google** | Android JVM — each thread has its own Java stack |
| **Qualcomm** | Snapdragon chips (most Android phones) — hardware stack support |

---

## ⚡ Time & Space Summary

| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| push | O(1) | O(n)* | O(n)* | O(1) |
| pop | O(1) | O(n)* | O(n)* | O(1) |
| peek | O(1) | O(1) | O(1) | O(1) |
| isEmpty | O(1) | O(1) | O(1) | O(1) |

> *O(n) because `insert(0, val)` shifts all elements. Use `append/pop()` from the end for true O(1).

---

## 💡 Pro Tip for Production

```python
# ❌ Slow — insert(0) is O(n)
stack.insert(0, value)
stack.pop(0)

# ✅ Fast — use end of list, O(1)
stack.append(value)
stack.pop()

# ✅✅ Best — collections.deque, thread-safe O(1)
from collections import deque
stack = deque()
stack.append(value)
stack.pop()
```

---

## 💡 Key Takeaway

> A stack is simple but **wildly powerful**. Every program running on your computer right now has a call stack executing. Every Ctrl+Z saves you via a stack. Every webpage navigation uses a stack. Every expression your compiler evaluates uses a stack. It's the invisible backbone of computing.

---

*Next up → Queue: the fair, orderly cousin of the stack* 🚶‍♂️🚶‍♀️🚶
