def rent(a):
    b = []
    z = len(a)
    for i in range(z):
        for j in range(i+1, z):
            for k in range(j+1, z):
                if a[i] + a[j] + a[k] == 0:
                    if [a[i], a[j], a[k]] not in b:
                        b.append([a[i], a[j], a[k]])
    return b

a = [-1, 0, 1, 2, -1, -4]
print(rent(a))
