a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
t=a[ran-1]
for i in range(ran-1,0,-1):
    l=a[i-1]
    a[i-1]=a[i]
    a[i]=l
a[0]=t
print(a)
