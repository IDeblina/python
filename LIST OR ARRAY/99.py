a=[]
b=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
print("Given array=")
print(a)
for i in range(ran):
    if(a[i]==0):
        b.append(a[i])
for i in range(ran):
    if(a[i]==1):
        b.append(a[i])
print("After segregation the array is =")
print(b)
