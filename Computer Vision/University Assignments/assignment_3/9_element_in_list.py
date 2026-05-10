my_list = [1,23,525,65,12,312,54,6,132,63]
num = int(input("Enter a number to check existence in list: "))
if num in my_list:
    index = my_list.index(num)
    print(f"{num} exists in list at index {index}")
else:
    print(f"{num} does not exist in list")