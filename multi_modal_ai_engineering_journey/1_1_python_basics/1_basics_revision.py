letter= '''Dear <|Name|>,
You are  selected!
<|Date|>
'''
print(letter)
# doubleSpace = letter.find("  ")
# replacedString = letter.replace("  ", " ")
# print(doubleSpace)
# print(replacedString)
# slicedString = letter[5:18]
# print(slicedString)

# slicedWithSkip = letter[0: 18 : 5]
# print(slicedWithSkip)


# print(letter)
# doubleSpace = letter.find("  ")
# replacedString = letter.replace("  ", " ")
# print(doubleSpace)
# print(replacedString)
# slicedString = letter[5:18]
# print(slicedString)

# slicedWithSkip = letter[0: 18 : 5]
# print(slicedWithSkip)

# sliceStart = letter[:18] # 0-(18-1)
# sliceEnd = letter[18:] #18 - end
# print(sliceStart)
# print(sliceEnd)


#  *********** String Functions ***********
# lengthOfString= len(letter)
# print("Length of string:", lengthOfString)

# endsWithString = letter.endswith("|>")
# print(endsWithString)

# startsWithString = letter.startswith("Dear")
# print(endsWithString)

# countCharacters = letter.count("r")
# print(endsWithString)

# capitalizeString = letter.capitalize()
# print(capitalizeString)

reversedString = letter[::-1]
print(reversedString)

letterLIst = list(letter)
letterLIst.reverse()
reversedBasedOnList = "".join(letterLIst)
print(reversedBasedOnList)

#  *********** Lists and List Functions ***********

myList = [10,12,34,4,5]
myList.sort()
myList.reverse()
myList.append(3)
myList.insert(0, 1)
myList.remove(10)
myList.pop(1)
print(myList)