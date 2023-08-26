n=int(input("Enter no."))
t=n
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==t):
    print("Perfect")
if(s>t):
    print("Abundant")
if(s<t):
    print("Defecient")
   
