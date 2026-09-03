from array import array
myFirstArray = array("i", [1,2,3,4,5,6,7,8,9,10])

copyArray = array(myFirstArray.typecode, (val for val in myFirstArray)) # generator expression
print(copyArray)

copyArray.pop(3)  # means index 3
copyArray.remove(5)  # means element 5 not index
print(copyArray)



#### Slicing 
slicedAray0_5 = copyArray[0:5]
print(slicedAray0_5)

slicedAray0_5_WithSteps = copyArray[0:5:2]
print(slicedAray0_5_WithSteps)

reversedArray = copyArray[::-1]
print(reversedArray)


arr1 = array("i", [1,2,3,4,5])
arr2 = array("i", [6,7,8,9,10])


arr1 = array("i", [1,2,3,4,5])
arr2 = array("i", [6,7,8,9,10])

arr1.extend(arr2)   # modifies arr1 in place

print(arr1)         # now this prints the combined array

print(arr1.itemsize)

arr1.tolist()
print(arr1)
