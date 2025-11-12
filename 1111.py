lst = [34,56, 34, 26,80, 57, 98, 100, 80, 64, 102, 300, 35, 6, 87,88]
count = 0
for i in range(len(lst) - 1):
    if (lst[i] >= 80) and (lst[i] <= 100):
        count += 1

print("Number of elements between 80 and 100:", count)

for  i in range(len(lst) - 1):
    if (lst[i] >= 80) and (lst[i] <= 100):
        item = lst[i]
        lst.remove(item)


print("List after removing elements between 80 and 100:", lst)