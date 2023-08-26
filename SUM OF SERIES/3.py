a=2
s=0
n=int(input("Enter range"))
for i in range(2,n+1):
    if(a%2==0):
        s=s+i
    else:
      	s=s-i
    a=a+1
print("Sum=",s)
