s=0
for i in range(1,1001):
    p=i
    while(p>9):
        n=p
        s=0
        while(n>0):
            r=int(n%10)
            s=s+r*r
            n=n//10
        p=s
    if(s==1):
        print(i,end=" ")
