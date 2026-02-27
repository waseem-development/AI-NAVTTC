data = {
    1: {"name": "Waseem"},
    2: {"scores": [85, 90, 78]}
}

# for i in range(0, len(data["scores"])):
    # print(data["scores"][i])



data[2]["scores"].append(100)
data.update({3: {"age": 23}})
# for score in data["scores"]:
#     print(score)

# print()

users = [
    {"name": "Waseem", "age": 22},
    {"name": "Lamiah", "age": 25}
]

users.append({"name": "Summiya", "age": 26})

for user in users:
    print(f"user: {user["name"]}, age: {user["age"]}")

print()

for index, info in data.items():
    print(f"{index} {info[""]}")