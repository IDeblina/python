a=1
b=1
s=0
n=int(input("Enter range"))
s=a+b
for i in range(1,n+1):
    c=a+b
    s=s+c
    a=b
    b=c
print("Sum=",s)
