number = int(input("Enter a number: "))

sum_n = 0
for count in range(1, number + 1):
    sum_n += count

print("Sum of numbers from 1 to", number, "=", sum_n)