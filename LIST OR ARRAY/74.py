r=int(input("Enter rows."))
c=int(input("Enter collumns."))
x=[[0 for i in range(r)]for j in range(c)]
if(r==c):
    for i in range(r):
        for j in range(c):
            print("Enter element",(i+1,j+1),end="=")
            x[i][j]=int(input())
    s=0
    for i in range(r):
        for j in range(c):
            if(i==j):
                s=s+x[i][j]
            
    print("Sum of the diagonal elemeents=",s)
else:
    print("Matrix should be Square ")

