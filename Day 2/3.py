def power(n):
    return n > 0 and (n & (n - 1)) == 0

n = int(input("Enter the number : "))
print(power(n))