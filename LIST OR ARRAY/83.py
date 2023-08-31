r=int(input("Enter row."))
c=int(input("Enter collumn."))
a=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        a[i][j]=int(input())
print("Original Array...")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print("")
for j in range(c):
    for i in range(r):
        for k in range(r-1):
            if(a[k][j]>a[k+1][j]):
                t=a[k][j]
                a[k][j]=a[k+1][j]
                a[k+1][j]=t
print("Sorted Array...")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print("")
