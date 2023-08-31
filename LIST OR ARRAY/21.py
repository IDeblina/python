n=int(input("Enter the range="))
a=[]
for i in range(n):
    a.append(int(input("Enter no.")))
s=0
p=1
for i in range(n):
    if(a[i]%2==0):
        s=s+a[i]
    else:
        p=p*a[i]
print("Sum of Even Numbers=",s)
print("Product of Odd Numbers=",p)
