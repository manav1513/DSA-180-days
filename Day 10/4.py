def randi(l):
    count = 0
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            count += 1
            if count > 1:
                return False
            if i > 0 and l[i + 1] < l[i - 1]:
                l[i + 1] = l[i]
            else:
                l[i] = l[i + 1]
    return True


l = [3,4,2,3]
print(randi(l))
