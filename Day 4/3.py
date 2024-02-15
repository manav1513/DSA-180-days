arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
arr3 = [5, 6, 7, 8, 9]

intersection = []

for num in arr1:
  
    if num in arr2 and num in arr3:
        intersection.append(num)

print(intersection)
