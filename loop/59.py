n=int(input("Enter no."))
t=n
s=0
l=0
while(n>0):
    n=int(n/10)
    l=l+1
if(l==10):
    while(t>0):
        r=int(t%10)
        s=s+r*l
        t=int(t/10)
        l=l-1
    if(s%11==0):
        print("legal ISBN")
    else:
        print("not ISBN")
else:
    print("No.should be of 10 digit")
