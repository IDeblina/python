def merge(x,m,y,n):
    for i in range(m):
        z.append(x[i])
    for j in range(n):
        z.append(y[j])
    print("Unsorted Z array")
    print(z)
    for i in range(m+n):
        for j in range(m+n-1):
            if(z[j]<z[j+1]):
                t=z[j]
                z[j]=z[j+1]
                z[j+1]=t
    print("Sorted z array")
    print(z)

x=[]
y=[]
z=[]
m=int(input("Input size of 1st array="))
for i in range(m):
    x.append(int(input("Enter no.")))
n=int(input("Input size of 2nd array="))
for i in range(n):
    y.append(int(input("Enter no.")))
merge(x,m,y,n)                     
