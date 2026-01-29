d = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True}
]

print("With Python 3.8 Walrus Operator:")
for entry in d:
    if name := entry.get("name"):
        print(name)

print("Without Walrus operator:")
for entry in d:
    name = entry.get("name")
    if name:
        print(name)