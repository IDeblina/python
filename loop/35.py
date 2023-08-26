n=int(input("Enter no"))
while(n>9):
    s=0
    n1=n
    while(n1>0):
        r=int(n1%10)
        s=s+r
        n1=int(n1/10)
    n=s
if(n==1):
    print("Magic no.")
else:
    print("not Magic no.")
        
    
