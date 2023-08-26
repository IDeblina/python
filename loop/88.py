a=0
b=1
for i in range(1,25):
    c=a+b
    c1=0
    for j in range(1,c+1):
        if(c%j==0):
            c1=c1+1
    if(c1==2):
        print(c,end=" ")
    a=b
    b=c
