a=[2,5,-1,6,-1,8,7,-1,9,1]
for i in range(10):
    for j in range(10):
        if(i==a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
print("First Condition..")
print(a)
for i in range(10):
    if(a[i]!=i):
        a[i]=-1
print("The new array is=")
print(a)
