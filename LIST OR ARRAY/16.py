a=[1,6,8,4,6]
m=a[0]
n=a[0]
for i in range(0,5):
    if(m<a[i]):
        m=a[i]
    if(n>a[i]):
        n=a[i]
print("Maximum is",m)
print("Minimum is",n)
