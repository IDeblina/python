print("Enter the row & coloumn")
r=int(input())
c=int(input())
x=[[0 for i in  range (r)]for j in range (c)]
y=[[0 for i in range (r)]for j in range (c)]
result=[[0 for i in range(r)]for j in range (c)]
print("Enter the value of 1st matrix.")
for i in range(0,r):
    for j in range(0,c):
        print('insert x[',i,',',j,']:',end=" ")
        x[i][j]=int(input())
print(x)
print("Enter the value of 2nd  matrix")
for i in range(0,r):
    for j in range(0,c):
        print('insert y[',i,',',j,']: ',end=" ")
        y[i][j]=int(input())
print(y)
print("SUM==")
for i in range(0,r):
    for j in range(0,c):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
        
