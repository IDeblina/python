a=[]
l=int(input("Enter range"))
for i in range(l):
    a.append(int(input("Enter value")))
m=a[0]
n=a[0]
for i in range(l):
    if(m<a[i]):
        m=a[i]
    if(n>a[i]):
        n=a[i]
print("Min=",n)
print("Max=",m)
    
