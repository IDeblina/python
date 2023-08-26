s=input("Enter no.")
n=int(s)
s2=s
d=0
if(len(s)<3):
    print("no. should be of atleast 3 digit")
else:
    for i in range(2,4):
        n1=n*i
        s2=s2+str(n1)
    p=int(s2)
    for i in range(1,10):
        num=p
        c=0
        while(num>0):
            r=int(num%10)
            if(r==i):
                c=c+1
            num=int(num/10)
        if(c==1):
            d=d+1
    if(d==9):
        print("Fascinating no.")
    else:
        print("not Fascinating no.")
