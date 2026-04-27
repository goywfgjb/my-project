items = [3, 7, 3, 9, 2, 7, 5, 8, 8, 1, 5]
print(items[-1])   # выведет 5

print(len(items))
print(sum(items))
print(items.index(9))

unique = []
for x in items:
    if x not in unique:
        unique.append(x)
print(unique)   # [3, 7, 9, 2, 5]