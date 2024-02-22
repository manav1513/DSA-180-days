# x = 'hello world'
# # m = 0
# # for i in range(0,len(x)):
# #     #print(i)
# #     if x[i:i+1] == " ":
# #         print(x[:-i])
    
#     # if i == ' ':
#     #     print(x[:i])
# t = x.split()
# print(len(t[-1]))
def cost(w):
    last = 0
    for i in range(len(w) - 1, -1, -1):
        if w[i] == " ":
            if last > 0:
                return last
        elif 'a' <= w[i] <= 'z':
            last += 1
        else:
            
            print("Invalid character found")
    return last

w = "hello world"
print(cost(w))