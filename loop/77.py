n=int(input("Enter no."))
d=l=0
while(n>0):
    r=int(n%10)
    c=0
    d=d+1
    for i in range(1,r+1):
        if(r%i==0):
            c=c+1
    if(c==2):
        l=l+1
    n=int(n/10)
if(l==d):
    print("All digit are prime")
else:
    print("All digit are not prime")
