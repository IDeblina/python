n=int(input("Enter no."))
p=int(input("Enter no."))
s=0
s1=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for i in range(1,p):
    if(p%i==0):
        s1=s1+i
if(s==p and s1==n):
    print("Amicable no.")
else:
    print("not amicable")
