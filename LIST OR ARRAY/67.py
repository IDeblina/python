a=[48,24,12,6]
d=0
n=int(input("Enter the number of Boxes="))
if(n>1000):
    print("Invalid Input")
else:
    l=n
    for  i in range(4):
        p=int(n/a[i])
        z=a[i]*p
        print(a[i],"*",p,"=",z)
        d=d+p
        n=n%a[i]
    print("Remaining Boxes=",n)
    print("Total Number of Boxes=",l)
    if(n==0):
        print("Total Number of cartons=",d)
    else:
        print("Total Number of cartons=",d+1)
    
        
