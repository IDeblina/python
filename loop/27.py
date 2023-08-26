n=int(input("Enter no."))
t=n
s=0
while(n>0):
    r=int(n%10)
    s=s+r
    n=int(n/10)
if(t%s==0):
    print("Harshad no.")
else:
    print("not Harshad")
            
