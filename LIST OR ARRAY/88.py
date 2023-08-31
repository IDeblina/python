a=[0,3,3,3,0,0,7,7,0,9]
a1=[]
for i in range(9):
    if(a[i]==a[i+1]):
        a[i]=2*a[i]
        a[i+1]=0
print("Doubled and replaced with zero..")
print(a)
for i in range(10):
    if(a[i]!=0):
        a1.append(a[i])
for i in range(10):
    if(a[i]==0):
        a1.append(a[i])
print("New Array..")
print(a1)
