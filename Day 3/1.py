def find_max_min(arr):
    if not arr:  
        return None, None

    
    max_num = min_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num


n = int(input("Enter the size of the array: "))
arr = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    arr.append(x)

max_num, min_num = find_max_min(arr)
print("Maximum element:", max_num)
print("Minimum element:", min_num)
