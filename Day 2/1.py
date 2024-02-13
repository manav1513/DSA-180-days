def reverse(x):
    str = str(x)[::-1]
    if x < 0:
       
       
        reversed_int = int(str[:-1]) * -1
    else:
        reversed_int = int(str)
    
    return reversed_int



num = 123
print("Original :", num)
print("Reversed :", reverse(num))  
