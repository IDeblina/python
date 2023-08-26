import math
s=1
a=2
p=2
n=int(input("Enter range"))
for i in range(1,n):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+ math.pow(a,p)/f
    p=p+1
print("Sum=",s)
