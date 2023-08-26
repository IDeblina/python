a=int(input("Enter no."))
n=a
length=0
t=a
a=a*a
while(n>0):
    n=int(n/10)
    length=length+1
x=int(a%pow(10,length))
y=int(a/pow(10,length))
if(t==x+y):
    print("kaprekar no.")
else:
    print("not Kapr.")
    
