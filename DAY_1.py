#1
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        print(j + 1, end=" ")
    print()  

#2
num = 1
row = 3
col = 3

for i in range(row):
    for j in range(col):
        print(num, end=" ")
        num += 1
    print() 

#3

r = 5

for i in range(1, r + 1):
    for j in range(i):
        print(i, end=" ")
    print()  

#4
for i in range(1, 6):
    print("* " * i)

    
