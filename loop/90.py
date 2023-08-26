for i in range(10000,100000):
    c=s=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        a=i
        while(a>0):
            r=int(a%10)
            s=s*10+r
            a=int(a/10)
    if(s==i):
        print(i,end=" ")
