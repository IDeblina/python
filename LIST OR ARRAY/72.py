a=[1,3,5,7,8]
b=[7,4,2,8,9]
t=[]
k=0
for i in range(5):
    for j in range(5):
        if(a[i]==b[j]):
            k=1
    if(k==1):
        t.append(a[i])
print("Intersection of Arrays=",end="")
print(t)
