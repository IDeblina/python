a=[]
for i in range(5):
    a.append(int(input("Enter number")))
print("Even Numbers=",end="")
for i in range(5):
    if(a[i]%2==0):
        print(a[i],end=" ")
print("")
print("Odd Numbers=",end="")
for i in range(5):
    if(a[i]%2==1):
        print(a[i],end=" ")
