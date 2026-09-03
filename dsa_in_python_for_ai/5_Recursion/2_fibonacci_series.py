# =========================
# Fibonacci — Recursive & Iterative
# =========================
# Series: 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# Rule:   fib(n) = fib(n-1) + fib(n-2)
#
# How to think recursively:
# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = 1  ← base case
# fib(1) = 1  ← base case
#
# Call tree for fib(5):
#                  fib(5)
#               /          \
#           fib(4)          fib(3)
#          /      \        /     \
#       fib(3)  fib(2)  fib(2)  fib(1)
#       /    \
#   fib(2)  fib(1)
#
# Notice: fib(3) calculated TWICE, fib(2) THREE TIMES
# This is why naive recursion is O(2^n) — exponential!


# ----------------- Recursive Version -----------------
def recursive_fibonacci(n):
    # Time:  O(2^n) — doubles with each call (very slow for large n)
    # Space: O(n)   — max depth of call stack

    if n < 1:
        return None                          # invalid input
    if n == 1 or n == 2:
        return 1                             # base case: fib(1) = fib(2) = 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# ----------------- Iterative Version -----------------
def iterative_fibonacci(n):
    # Time:  O(n) — single loop
    # Space: O(1) — only two variables, no call stack buildup

    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1                             # fib(1)=1, fib(2)=1
    for _ in range(3, n + 1):              # start from fib(3)
        a, b = b, a + b                     # slide window forward
    return b


# ----------------- Memoized Version (Best of Both) -----------------
def memoized_fibonacci(n, memo={}):
    # Time:  O(n) — each value calculated ONCE and cached
    # Space: O(n) — memo dict + call stack

    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]                      # already calculated, reuse it!
    memo[n] = memoized_fibonacci(n - 1, memo) + memoized_fibonacci(n - 2, memo)
    return memo[n]


# ----------------- Print Full Series -----------------
def print_series(n):
    print(f"Fibonacci series up to {n} terms:")
    series = [str(iterative_fibonacci(i)) for i in range(1, n + 1)]
    print(" → ".join(series))


# =========================
# Interactive Program
# =========================
print("=" * 45)
print("      Fibonacci Number Calculator")
print("=" * 45)
print("Options:")
print("  Enter a number → find its Fibonacci value")
print("  's'            → print the full series")
print("  '-1'           → exit\n")

while True:
    try:
        user_input = input("Enter a number (or 's' for series, -1 to exit): ").strip()

        # Exit
        if user_input == '-1':
            print("Goodbye!")
            break

        # Print full series
        if user_input.lower() == 's':
            terms = int(input("How many terms? "))
            if terms <= 0:
                print("Please enter a positive number!\n")
                continue
            print_series(terms)
            print()
            continue

        num = int(user_input)

        if num <= 0:
            print("Please enter a positive number! Fibonacci is defined for n ≥ 1\n")
            continue

        # Warn user before running slow recursive on large input
        if num > 30:
            print(f"⚠️  Warning: Recursive is very slow for n={num} (O(2^n))")
            print(f"   Showing Iterative and Memoized only for large n.\n")
            recur_result = recursive_fibonacci(num)
            iter_result = iterative_fibonacci(num)
            memo_result = memoized_fibonacci(num)
            print(f"Simple Recursive : fib({num}) = {iter_result}")
            print(f"Iterative : fib({num}) = {iter_result}")
            print(f"Memoized  : fib({num}) = {memo_result}\n")
        else:
            rec_result  = recursive_fibonacci(num)
            iter_result = iterative_fibonacci(num)
            memo_result = memoized_fibonacci(num)
            print(f"Recursive : fib({num}) = {rec_result}")
            print(f"Iterative : fib({num}) = {iter_result}")
            print(f"Memoized  : fib({num}) = {memo_result}\n")

    except ValueError:
        print("Please enter a valid integer!\n")
    except RecursionError:
        print("Number too large for recursion! Try iterative or memoized instead.\n")