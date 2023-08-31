r=int(input("Enter rows"))
c=int(input("Enter collums"))
if(r%2==1):
    print("Row must be Even for Interchange")
else:
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
        t=a[int(r/2)][j]
        a[int(r/2)][j]=a[int(r/2)-1][j]
        a[int(r/2)-1][j]=t
print("New Matrix...")
for i in range(r):
        for j in range(c):
            print(a[i][j],end=" ")
        print("")
