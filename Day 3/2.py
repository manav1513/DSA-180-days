def rev(lt, n):
    i = 0
    j = n - 1

    while j > i:
        lt[i], lt[j] = lt[j], lt[i]
        i += 1
        j -= 1
    return lt

n = int(input("Enter the size of the array: "))
lt = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    lt.append(x)
print(rev(lt, n))
