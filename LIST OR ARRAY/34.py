r=int(input("Enter row"))
c=int(input("Enter collumn"))
x=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        x[i][j]=int(input())

y=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        y[i][j]=int(input())
s=0
mul=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        for k in range(r):
            s=s+x[i][k]*y[k][j]
        mul[i][j]=s
        s=0
print('First Matrix:',x)
print('Second Matrix:',y)
print('Product is:',mul)

