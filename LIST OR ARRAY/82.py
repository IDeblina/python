r=int(input("Enter row."))
c=int(input("Enter collumn."))
a=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        a[i][j]=int(input())
for i in range(c):
    s=0
    for j in range(r):
        s=s+a[j][i]
    print("Sum of elements of Collumn",i+1,"=",s)
    
    
