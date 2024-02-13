def find(n):
    
    str = bin(n)[2:]
    
    complement = ''.join(['0' if bit == '1' else '1' for bit in str])
    
    complement_int = int(complement, 2)
    
    return complement_int


n = int(input("enter the number :"))
print(find(n))

