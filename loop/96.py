n=int(input("Enter range"))
s=c=j=0
for i in range(1,n+1):
    s=i
    j=i+1
    while(s<n):
        s=s+j
        j=j+1
    if(s==n):
        for k in range(i,j+1):
            if(k==i):
                print(k)
            else:
                print("+",k)
                
