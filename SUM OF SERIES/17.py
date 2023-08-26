import math
a=3
s=0
n=int(input("Enter range"))
for i in range(1,n+1):
    s=s+(math.pow(a,i))/i  
print(s)
        
