s=s1=0
n=int(input("Enter no."))
while(n>0):
    r=int(n%10)
    s=s+r
    n=n//10
t=n
for i in range(1,n+1):
    c=0
    if(n%i==0):
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c==2):
            s1=s1+i
if(s==s1):
    print("Smith no.")
else:
    print("not Smith no.")
            
