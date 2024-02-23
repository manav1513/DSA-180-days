l = [1, 2, 3, 1]
found = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            found = True
            break
    if found:
        break

print(found)
