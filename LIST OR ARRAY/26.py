a=[]
s=0
n=int(input("Enter range="))
for i in range(n):
    a.append(int(input("Enter no.")))
print("Magic Numbers are=",end="")
for i in range(n):
    l=a[i]
    while(l>9):
        num=l
        s=0
        while(num>0):
            r=num%10
            s=s+r
            num=int(num/10)
        l=s
    if(s==1):
            print(a[i],end=" ")
