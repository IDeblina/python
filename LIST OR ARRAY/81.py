r=int(input("Enter row."))
c=int(input("Enter collumn."))
a=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        a[i][j]=int(input())
for i in range(r):
    s=0
    for j in range(c):
        s=s+a[i][j]
    print("Sum of elements of Row",i+1,"=",s)
    
    
