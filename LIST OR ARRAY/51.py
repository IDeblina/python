def merge(x,m,y,n):
    z=[]
    for i in range(m):
        z.append(x[i])
    for i in range(n):
        z.append(y[i])

    for j in range(0,m+n):#used bubble sort
        for i in range(0,m+n-1):
        
            if(z[i]<z[i+1]):
                t=z[i]
                z[i]=z[i+1]
                z[i+1]=t
    print(z)





x=[3,2,1]
y=[6,5,4,3]
merge(x,3,y,4)
