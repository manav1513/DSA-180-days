l = [2, 7, 11, 15]
t = 9  # Adjusted to a valid value
i = 0
while i < len(l):
    j = i + 1  
    while j < len(l):
        if l[i] + l[j] == t:
            print([l[i], l[j]])
        j += 1
    i += 1
