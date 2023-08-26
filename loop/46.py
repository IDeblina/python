n=int(input("Enter no."))
b=1
s=0
while(n>0):
    r=int(n%2)
    s=s+r*b
    n=n//2
    b=b*10
print("Binary",s)
