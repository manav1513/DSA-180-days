arr = [1, 2, 3, 5, 4, 4, 3, 3, 1]

counts = {}
for num in arr:
    counts[num] = counts.get(num, 0) + 1

res = [num for num, count in counts.items() if count == 2]

print(res)
