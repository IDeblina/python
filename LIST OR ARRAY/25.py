a=[]
for i in range(5):
    a.append(int(input("Enter no.")))
print("Armstrong Numbers Are=",end="")
for i in range(5):
    n=a[i]
    s=0
    while(n>0):
        r=n%10
        s=s+r*r*r
        n=int(n/10)
    if(s==a[i]):
        print(a[i],end=" ")
        
