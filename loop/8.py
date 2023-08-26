a=int(input("Enter no."))
s=0
c1=0
c2=0
for i in range(1,a+1):
    if(a%i==0):
        c1=c1+1
if(c1==2):
    while(a>0):
        r=int(a%10)
        s=s*10+r
        a=int(a/10)
for i in range(1,s+1):
    if(s%i==0):
        c2=c2+1
if(c2==2):
    print("Twisted prime")
else:
    print("not twisted prime")
        
