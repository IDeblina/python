n=int(input("Enter a no."))
#p=n
s=0
t=1
while(n>0):
    r=int(n%10)
    s=s+r
    t=t*r
    n=n//10
if(s==t):
    print("Sum-product")
else:
    print("not Sum-product")
