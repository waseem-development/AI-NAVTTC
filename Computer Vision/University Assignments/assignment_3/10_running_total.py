my_list = [1, 23, 24, 100]
running_total = []
total = 0
for num in my_list:
    total+=num
    running_total.append(total)
print(f"Running total: {running_total}")
