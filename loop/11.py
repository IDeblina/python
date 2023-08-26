import math
a=int(input("Enter no."))
b=int(input("Enter no."))
c1=0
c2=0
for i in range(1,a+1):
    if(a%i==0):
        c1=c1+1
for i in range(1,b+1):
    if(b%i==0):
        c2=c2+1
d=math.fabs(a-b)
if(c1==2 and c2==2 and d==2):
    print("Twin Prime")
else:
    print("not Twin Prime")       
        
