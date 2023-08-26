n=int(input("Enter no."))
t=n
l=0
s=0
while(n>0):
    n=n//10
    l=l+1
if(l==5):
    p=int(t%100)
    x=int(p%10)
    y=int(p/10)
    while(t>0):
        r=int(t%10)
        s=s+r
        t=int(t/10)
    if(s==36 and x*y==32):
        print("Flappy")
    else:
        print("not Flappy")
else:
    print("No. should be 5 digit") 
