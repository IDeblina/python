def transfer(a,b,n):
    for i in range(n):
        if(a[i]<0):
            b.append(a[i])
    for i in range(n):
        if(a[i]>0):
            b.append(a[i])
    for i in range(n):
        if(a[i]==0):
            b.append(a[i])
    
    print(b)
a=[]
b=[]
ran=int(input("Enter range="))
for j in range(ran):
    a.append(int(input("Enter no.")))
transfer(a,b,ran)
