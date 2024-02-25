def h(l):
    counter = 0
    for i in range(len(l)-1):
        #print(l[i])
        #if counter == 2:
            #return "False"
        if not(l[i]<=l[i+1]):
            counter +=1
            if counter == 2:
                return "False"
    return "True"
print(h([3,4,2,3]))