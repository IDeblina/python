n=int(input("Enter no."))
s=0
t=n
while(n>0):
    r=int(n%10)
    s=s+r*r*r
    n=int(n/10)
if(s==t):
    print("Armstrong")
else:
    print("not armstrong")
