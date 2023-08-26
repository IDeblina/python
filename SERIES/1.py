a=4
b=3
n=int(input ("Enter the limit:"))
for i in range(1,n+1):
    print(a,end=" ")
    a=a+b
    b=b+2
print("...",end=" ")
