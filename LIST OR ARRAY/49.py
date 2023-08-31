a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
for i in range(ran):
    if(a[i]%2==0):
        a[i]=a[i]*2
    else:
        a[i]=a[i]*3
print(a)
