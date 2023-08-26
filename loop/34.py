n=int(input("Enter a no."))
p=1
while(n>0):
    r=int(n%10)
    p=p*r
    n=n//10
print(p)
