a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
print("Niven Numbers are=")
for i in range(ran):
    n=a[i]
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=int(n/10)
    if(a[i]%s==0):
        print(a[i],end=" ")
        
        
