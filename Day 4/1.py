# def match(n , lt):

#     i = 0
#     j = len(lt)

#     while i>j:

#         for i in lt(0, n+1):
#             print(i)

#             for j in lt(i+1,n):
#                 print(j)
#                 if i == j:
#                     return True
#                 else:
#                  j = j + 1
#             i = i + 1


n = int(input("Enter the size of the array: "))
lt = []
for i in range(0, n):
    x = int(input("Enter element for list: "))
    lt.append(x)
print("The entered list is :", lt)
counter = 0

for i in lt:
    

    for j in range(i+1,n):
        
     
        if lt[i] == lt[j]:
              counter +=1

if counter != 0:
    print ("true")
else:
    print ("false")


