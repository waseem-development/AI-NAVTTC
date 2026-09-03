# Recursion: When a function invokes (calls) itself
# Iterative Code can be converted to Recursive code and benefits are that 
# the same logic will be easier in recursion and even code will be smaller 
# (loops make it a bit longer and harder)

# How to know that can I solve this particular problem with recursion or not?
# Answer: Can this problem divided into smaller chunks at each iteration (recursive call)
# OR can this problem be divided into chunks?
# This is possible with loops but also recursion

# To understand recursion problem: 
# 1) Starting Point
# 2) Logic
# 3) Terminating Condition (otherwise infinite recursion or no output)

# - Factorial of a number
# In recursion if you have a problem (bigger) then keep dividing into chunks untill u recieve a very small chunk that u already know the answer to (base case will tell u your terminating condition)
# factorial (5)  = 5 * factorial (5-1 (4)) ==> Generalize it
# factorial (n)  = n * factorial (n-1) ==> Generalize it
# Recursive version
# Factorial (4) ==> 4 *factorial (4-1 (3)) but do not execute and make a copy of another function with eaxtly the same code in memory for factorial (3) == > 3 *factorial (2-1 (2)) but do not execute and make a copy of another function with eaxtly the same code in memory for factorial (2) == > 2*factorial (2-1 (1)) now make a copy for factorial(1) withuot executing earlier codes
# Now for factorial (1) since this is our terminating condition i.e (  if n == 0 or n == 1:) so we return the statement and now we go to factorail (2) and memory will be relieased for factorial (1) and it become 2*1 = 2 then go to factorial (3) which now become 3*2 = 6 now move to factorial (4) which now becomes 4 * 6 = 24 so factorial of 4 is 24
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return None
    return n * recursive_factorial(n - 1)

# Iterative version (fixed)
def iterative_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    fact = 1
    for i in range(2, n + 1):  # Start from 2 to n
        fact *= i
    return fact

# Test both
while True:
    try:
        num = int(input("Enter a number to find factorial (-1 to exit): "))
        
        if num == -1:
            print("Goodbye!")
            break
        
        if num < 0:
            print("Factorial not defined for negative numbers!\n")
            continue
        
        # Test both methods
        rec_result = recursive_factorial(num)
        iter_result = iterative_factorial(num)
        
        print(f"Recursive: {num}! = {rec_result}")
        print(f"Iterative: {num}! = {iter_result}\n")
        
    except ValueError:
        print("Please enter a valid integer!\n")
    except RecursionError:
        print("Number too large for recursion! Try a smaller number.\n")