a=0
b=0
c=1
for i in range(1,25):
    d=a+b+c
    c1=0
    for j in range(1,d+1):
        if(d%j==0):
            c1=c1+1
    if(c1==2):
        print(d,end=" ")
    a=b
    b=c
    c=d
