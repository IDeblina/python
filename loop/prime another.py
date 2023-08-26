n=int(input("Enter the no"))
i=2
while(i<n):
    if(n%i==0):
        print("not prime")
        break;
    i=i+1
if(n==i+1):
    print("prime")
