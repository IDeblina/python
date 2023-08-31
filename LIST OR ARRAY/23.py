a=[]
for i in range(5):
    a.append(int(input("Enter no.")))
m=a[0]
n=a[0]
s=0
for j in range(5):
    if(m<a[j]):
       m=a[j]
    if(n>a[j]):
       n=a[j]
    s=s+a[j]
print("MAX=",m)
print("MIN=",n)
print("SUM=",s)
