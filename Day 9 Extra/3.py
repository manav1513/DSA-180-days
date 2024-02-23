def addB(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry:
        da = int(a[i]) if i >= 0 else 0
        db = int(b[j]) if j >= 0 else 0

        sum = da + db + carry
        carry = sum // 2
        result = str(sum % 2) + result
        i -= 1
        j -= 1
    
    return result

a = "11"
b = "1"
print( addB(a, b))

