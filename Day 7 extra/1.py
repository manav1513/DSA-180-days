def remove(arr):
    u = []
    h=[]
    for i in arr:
        if i not in u:
            u.append(i)
        else:
            h.append(i)

    for s in range(len(u),len(arr)):
        u.append("_")
    
    return u



n = int(input("Enter the size of the array: "))
arr = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    arr.append(x)
print(remove(arr))
# arr = remove(arr)
# print(len(arr) , )

