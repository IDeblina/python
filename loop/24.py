a=int(input("Enter no."))
c=0
while(a>0):
    r=int(a%10)
    if(r==0):
        c=c+1
    else:
        rev=r
    a=int(a/10)
if(c>0):
    print("Duck no.")
else:
    print("not Duck no.")
