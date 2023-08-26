for i in range(100,1001):
    length=0
    n=i
    t=i
    a=i*i
    while(n>0):
        n=int(n/10)
        length=length+1
    x=int(a%int(pow(10,length)))
    y=int(a/int(pow(10,length)))
    if(t==x+y):
        print(i,end=" ")
