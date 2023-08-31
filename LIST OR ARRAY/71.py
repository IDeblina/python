a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(0,10,2):
    t=a[i]+a[i+1]
    b.append(t)
print(b)
