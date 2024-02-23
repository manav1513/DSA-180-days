def rent(a):
    i=0
    j=1
    z=1
    ans=[]
    while(i!=len(a)):
        #for j in range(i+1,len(a)):
            #print(f''' z :{z} | i :{i} | j :{j} | len(a) :{len(a)}''')
        if z!= len(a)-1:
            z+=1
            if a[i] + a[j] + a[z] == 0:
                ans.append([a[i],a[j],a[z]])
            elif a[i]+a[j]+a[z]!=0 and j==len(a)-1:
                j+=1
            elif  a[i]+a[j]+a[z]!=0 and i==len(a)-2 and j==len(a)-1 and z!=len(a)-3:
                i+=1
        else:
            z=j+1
    return ans

a = [-1, 0, 1, 2, -1, -4]
print(rent(a))