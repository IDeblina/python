s=0
a=1
b=2
n=int(input("Enter range"))
for i in range(1,n+1):
    s=s+(a/b)
    a=a+1
    b=b+1
print("Sum=",s)
