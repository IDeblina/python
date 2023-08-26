a=0
b=1
for i in range(1,25):
    c=a+b
    if(c%2==0):
        print(c,end=" ")
    a=b
    b=c
