n = int(input("Enter the size of the array: "))
ar = []
for _ in range(n):
    x = int(input("Enter element: "))
    ar.append(x)
print("Original array:", ar)


zero = []
non_zero = []
for i in ar:
    if i == 0:
        zero.append(i)
    else:
        non_zero.append(i)

ar = non_zero + zero  

print(ar)

    