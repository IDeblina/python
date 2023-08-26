import math
n=int(input("Enter no"))
l=0
s=0
t=n
t1=n
while(n>0):
    n=n//10
    l=l+1
while(t>0):
    r=int(t%10)
    s=s+math.pow(r,l)
    t=t//10
    l=l-1
if(s==t1):
    print("Disarium no.")
else:
    print("not Disarium no.")
