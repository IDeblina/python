import math
a=int(input("Enter a's value:"))
n=int(input("Enter range:"))
s=0
b=2
k=2
for i in range(1,n+1):
    if(k%2==0):
        s=s+(a/math.factorial(b))
    else:
        s=s-(a/math.factorial(b))
    b=b+1
    k=k+1
print(s)
