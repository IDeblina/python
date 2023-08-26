n=int(input("Enter no."))
s=0
while(n>0):
    r=int(n%10)
    s=s+r
    n=int(n/10)
print("Sum of digit=",s)
