for i in range(1,1001):
    n=i
    s=0
    while(n>0):
        r=int(n%10)
        s=s+r*r*r
        n=int(n/10)
    if(s==i):
        print(i,end=" ")
        
        
