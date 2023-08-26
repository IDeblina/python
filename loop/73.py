n=int(input("Enter range"))
s=l=0
for i in range(1,n+1):
    n1=int(input("Enter no."))
    if(n1%2==0):
        s=s+n1
        l=l+1
avg=s/l
print("Avg.=",avg)
    
