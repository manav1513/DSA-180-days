def pala(x):
    x = str(x)
    return x == x[::-1]


def is_palindrome(x):
    if x < 0:
        return False
    
    original = x
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10

    return original == reverse

x = int(input("Enter the palindrome number: "))
print(is_palindrome(x))
