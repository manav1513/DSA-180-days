n = int(input("Enter the size of the array: "))
arr = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    arr.append(x)

arr = arr[::-1]
print(arr)

       