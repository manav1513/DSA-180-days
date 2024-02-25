def h(l):
    counter = 0
    for i in range(0,len(l)-1):
        #print(l[i])
        #if counter == 2:
            #return "False"
        if not(l[i]<l[i+1]):
            counter +=1
            if counter == 2:
                return "False"
    return "True"
print(h([5,7,1,8]))