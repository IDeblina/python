n=int(input("Enter no."))
d=0
t=n
for i in range(0,10):
    num=n
    c=0
    while(num>0):
        r=int(num%10)
        if(r==i):
            c=c+1
        num=int(num/10)
    if(c==1):
         d=d+1
if(len(str(t))==d):
    print("Unique no.")
else:
    print("not Unique no.")
