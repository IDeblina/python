n=int(input("Enter no."))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
        print(i,end=" ")
print("Count=",c)
