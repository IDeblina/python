a=int(input("Enter a no."))
s=rev=p=0
while(a>0):
    r=int(a%10)
    if(r==0):
        p=r
    else:
        rev=rev*10+r
    a=int(a/10)

while(rev>0):
    r=int(rev%10)
    s=s*10+r
    rev=int(rev/10)
print("After removing zero=",s)
