a=9
b=99
s=0
n=int(input("Enter range"))
for i in range(1,n+1):
    c=a+b
    s=s+c
    a=a-1
    b=b-10
print("Sum=",s)
    
