a=[]
for i in range(5):
    a.append(int(input("Enter  No.")))
print("Special Numbers are=",end="")
for i in range(5):
    n=a[i]
    s=0
    while(n>0):
        r=n%10
        p=1
        for k in range(1,r+1):
            p=p*k

        s=s+p
        n=int(n/10)
    if(s==a[i]):
        print(a[i],end=" ")
