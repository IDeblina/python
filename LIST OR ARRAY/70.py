a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[]
i,j,k=0,0,0

while(i<len(a)+len(b)):
    if i%2==0:
        c.append(a[k])
        print(c)
        k+=1
    else:
        c.append(b[j])
        j+=1
        print(c)

    i+=1
print(c)
