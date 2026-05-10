def binary_search(my_list, key, size):
    my_list.sort()
    start = 0
    end = size - 1
    
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] < key:
            start = mid + 1
        elif my_list[mid] > key:
            end = mid - 1
        else:
            return mid
    return -1

my_list = [0,7,2,9,36,18,128,65,8,10,30,21]
key = int(input("Enter the key to search in the list: "))
size = len(my_list)

result = binary_search(my_list, key, size)

if result == -1:
    print("Element not found in the list.\n");
else:
    print(f"Element {key} found at index {result}.")