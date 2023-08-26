s=0
a=1
b=2
n=int(input("Enter range"))
for i in range(1,n+1):
    a=a*b
    s=s+a+i
    b=b+1
print("Sum=",s)    
    
