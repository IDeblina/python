n=int(input("Enter no."))
while(n>9):
    p=n
    s=0
    while(p>0):
        r=int(p%10)
        s=s+r*r
        p=int(p/10)
    n=s
if(s==1):
    print("Happy no.")
else:
    print("not Happy no.")
    
