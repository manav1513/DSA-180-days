# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# n = int(input("Enter the size of the aay: "))
# a = []
# for i in range(0, n):
#     x = int(input("Enter element for list: "))
#     a.append(x)

a = [1,2,2,3]
v = 2
u = []
for i in a:
    if i != v:
        u.append(i)
# print(len(a), len(u))
# print(u)


for s in range(len(u),len(a)):
        u.append("_")
print(len(u),u)