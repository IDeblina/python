import math
s=0
n=int(input("Enter range"))
a=int(input("Enter a's value"))
for i in range(1,n+1):
    s=s+(i/(math.pow(a,i)))
print(s)
    
