s=0
e=1
f=2
a=2
n=int(input("Enter range"))
for i in range(1,n+1):
    s=s+((a+e)/f)
    e=e+2
    f=f+2
print("Sum=",s)
