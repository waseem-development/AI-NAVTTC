# import array as arr
from array import array
myFirstArray = array("i", [1,2,3,4,5,6,7,8,9,10])

myFirstArray.append(11)
myFirstArray.append(12)
myFirstArray.append(13)
print(f"myFirstArray = {myFirstArray}")
print(f"myFirstArray[0] = {myFirstArray[0]}")
print(f"myFirstArray[11] = {myFirstArray[11]}")
print(f"myFirstArray[4] = {myFirstArray[4]}")


# for i, element in enumerate(myFirstArray):
#     print(f"{i+1}) {element}", end=" ")

# for element in range(0, len(myFirstArray)):
#     print(f"{element}", end=", ")

myFirstArray.insert(len(myFirstArray), 14)
print("{",end="")
for i in range(len(myFirstArray)):
    if i == len(myFirstArray) - 1:
        print(f"{myFirstArray[i]}", end="")
    else: 
        print(f"{myFirstArray[i]}", end=", ")
print("}",end="")
print(f"\n*****\nmyFirstArray typecode: {myFirstArray.typecode}\n*****\n")