s=0
n=int(input("Enter range"))
for i in range(1,n+1):
    s=s+(i+(i+1))/((i+1)*(i+2))
print("Sum=",s)
