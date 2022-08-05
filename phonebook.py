from cs50 import get_string

people = {
    "hesham": "01111111",
    "saad": "0122222222",
    "mohamed": "0155555555"
}

name = get_string("name: ")
if name in people:
    print(f"Found: {people[name]}")
else:
    print("Not found")
