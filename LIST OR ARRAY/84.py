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
print("New Arranged Array...")
for i in range(r):
    for j in range(c):
        if(j>=i):
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")
