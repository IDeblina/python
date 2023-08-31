a=[]
b=[]
r=int(input("enter the range="))
for i in range(0,r):
    a.append(int(input("enter the number=")))
for i in range(r-1,-1,-1):
    b.append(a[i])
print(b)
