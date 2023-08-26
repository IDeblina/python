import math
n=int(input("Enter no/"))
s=0
t=n
while(n>0):
    r=int(n%10)
    s=s+math.factorial(r)
    n=int(n/10)
if(t==s):
    print("Krishnamurthy no.")
else:
    print("not Krishnamurthy no.")
    
    
