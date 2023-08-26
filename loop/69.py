n=int(input("Enter no."))
s=p=rev=0
while(n>0):
    r=int(n%10)
    if(r%2!=0):
        p=r
    else:
        rev=rev*10+r
    n=int(n/10)
while(rev>0):
    r=int(rev%10)
    s=s*10+r
    rev=int(rev/10)
print("No. without odd digit",s)
