nums = [2,0,2,1,1,0]
z = []
o = []
t = []

for i in nums:
    if i == 0:
        z.append(i)
    elif i == 1:
        o.append(i)
    else : 
        t.append(i)
num = list(z + o + t)
print(num)
