n=int(input("Enter no."))
s=0
p=1
while(n>0):
    r=int(n%10)
    s=s+r
    p=p*r
    n=n//10
if(s==p):
    print("Spy no.")
else:
    print("not Spy no.")
    

      
