n=int(input("Enter no."))
s=0
while(n>0):
    r=int(n%10)
    c=0
    for j in range(1,r+1):
        if(r%j==0):
            c=c+1
    if(c==2):
        s=s+r
    n=n//10
print(s)
