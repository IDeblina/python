n=int(input("Enter no."))
b=1
s=c=0
while(n>0):
    r=int(n%2)
    s=s+r*b
    n=n//2
    b=b*10
while(s>0):
    r=int(s%10)
    if(r==1):
        c=c+1
    s=s//10
if(c%2==0):
    print("Evil no.")
else:
    print("not Evil no.")
        
