n = int(input("Enter the size of the array: "))
arr = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    arr.append(x)

k = int(input("Enter the shift : "))

while k > 0:
    last_element = arr[-1]
    arr.insert(0, last_element)
    arr = arr[:-1]
    k = k - 1

print(arr)