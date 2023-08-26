s=0
y=2
n=int(input("Enter range"))
for i in range(2,n+1):
    if(y%2==0):
        s=s-(i/(i+1))
    else:
        s=s+(i/(i+1))
    y=y+1
print("Sum=",s)
