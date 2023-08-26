s=0
a=1
b=1
n=int(input("Enter range"))
for i in range(1,n+1):
    s=s+a/(b*b)
    a=a+2
    b=b+1
print("Sum=",s)
