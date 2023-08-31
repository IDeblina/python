m=int(input("Enter row."))
n=int(input("Enter collumn."))
x=[[0 for i in range(m)]for j in range(n)]
if(m>11 or m<2 or n<2 or n>11):
    print("Matrix size out of range")
else:
    for i in range(m):
        for j in range(n):
            print("Enter element",(i+1,j+1),end="")
            x[i][j]=int(input())
    print("Original Matrix....")
    print(x)
    for i in range(0,m):
        for j in range(0,n):
            for k in range(0,n-1):
                if(x[i][k]>x[i][k+1]):
                    t=x[i][k]
                    x[i][k]=x[i][k+1]
                    x[i][k+1]=t
    print("Matrix after sorting rows....")
    print(x)
        
