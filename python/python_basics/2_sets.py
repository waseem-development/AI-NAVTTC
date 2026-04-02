mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
mySet.add(5)

print("mySet: ", mySet, "\n")

print("Length of mySet: ",len(mySet), "\n")

print(mySet.remove(4), "\n")

print("Removed: ",mySet.pop(), "\n")

print("mySet: ",mySet, "\n")

newSetUnion = mySet.union({3,5,9,10})

print("Union: ",newSetUnion, "\n")

newSetIntersection = newSetUnion.intersection({3,5,10})

print("Intersection: ", newSetIntersection)

newSet = set()
newSet.add(18)
newSet.add("18")
print("\n",newSet)
print(type(newSet))