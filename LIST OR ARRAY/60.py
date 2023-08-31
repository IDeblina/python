r=int(input("Enter rows"))
c=int(input("Enter collums"))
a=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
            print("Enter element",(i+1,j+1))
            a[i][j]=int(input())
print("Old Matrix...")
for i in range(r):
        for j in range(c):
            print(a[i][j],end=" ")
        print("")
for j  in range(c):
        t=a[0][j]
        a[0][j]=a[r-1][j]
        a[r-1][j]=t
print("New Matrix...")
for i in range(r):
        for j in range(c):
            print(a[i][j],end=" ")
        print("")
