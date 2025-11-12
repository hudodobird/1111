names_list = ["James", "Susan", "Rob", "Katie"]
print(names_list)

names_list.insert(0, "Ryan")
print(names_list)

names_list.pop(1)
print(names_list)

while len(names_list) < 7:
    name = input("Enter a name to add to the list: ")
    names_list.append(name)

print(names_list)