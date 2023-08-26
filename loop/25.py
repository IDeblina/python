a=int(input("Enter no."))
t=a
s=0
c=0
for i in range(1,a+1):
    if(a%i==0):
        c=c+1
if(c==2):
    while(a>0):
        r=int(a%10)
        s=s*10+r
        a=int(a/10)
if(s==t):
    print("prime palindrome")
else:
    print("not prime palindrome")
