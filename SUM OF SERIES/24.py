import math
s=0
b=1
c=1
j=2
n=int(input("Enter range"))
a=int(input("Enter a's value"))
for i in range(1,n+1):
    if(j%2==0):
        s=s+(math.pow(a,b)/c)
    else:
        s=s-(math.pow(a,b)/c)
    b=b+2
    c=c+4
    j=j+1
print(s)
    
