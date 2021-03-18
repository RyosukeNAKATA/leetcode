l = [1, 2, 3, 4, 5]
for j in range(4):
    print(j)
    if l[j] == 3:
        l.pop(j)

print(l)