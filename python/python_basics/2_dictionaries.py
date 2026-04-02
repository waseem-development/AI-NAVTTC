myDictionary = {
    "name": "Hafiz Waseem Ahmed",
    "email": "waseemdeelopment2002@gmail.com",
    "password": "W********************1",
    "tasks": ["Work Hard", "Develop Skills", "Build Career"]
}

myDictionary.update({"financialGoal":"Financial Stability"})
myDictionary.update(long_term_goal="Professional Excellence")
print(myDictionary.get("tasks"), "\n\n\n")
# print(myDictionary["name"])
# print(myDictionary["email"])
# print(myDictionary["password"])
# print(myDictionary["wife"])
# print(myDictionary["tasks"][0])
# print(myDictionary["tasks"][1])
# print(myDictionary["tasks"][2])

# keyLists = list(myDictionary.keys())

# print(keyLists)
# print(keyLists[0])
# print(keyLists[1])
# print(keyLists[2])
# print(keyLists[3])
# print(myDictionary.items())

# print(myDictionary.keys())
# print(myDictionary.values())

# for attribute, data in myDictionary.items():
#     print(f"{attribute}: {data}")


# for key in myDictionary:
#     print(key)

# for key in myDictionary.keys():
#     print(key)

# for attribute in myDictionary.values():
#     print(attribute)


# for attribute in sorted(myDictionary):
#     print(attribute, myDictionary[attribute])

for attribute in reversed(myDictionary):
    print(attribute, myDictionary[attribute])

myDictionary.pop("password")
print("\n\n\n")
for attribute in myDictionary.values():
    print(attribute)

del myDictionary["tasks"]
print("\n\n\n")
for attribute in myDictionary.values():
    print(attribute)
