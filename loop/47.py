n=int(input("Enter no."))
s=0
b=1
while(n>0):
    r=int(n%10)
    s=s+b*r
    n=n//10
    b=b*2
print("Decimal=",s)
