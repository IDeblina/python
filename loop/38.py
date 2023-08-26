n=int(input("Enter no."))
s=0
for i in range(1,n+1):
    if(n%i==0):
        s=s+i
        print(i,end=" ")
print("Sum of factors=",s)
