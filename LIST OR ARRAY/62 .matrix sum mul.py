print("Enter the row & coloumn")
m1=int(input())
n1=int(input())
x=[[0 for i in  range (n1)]for j in range (m1)]
y=[[1 for i in range (n1)]for j in range (m1)]
result=[[0 for i in range (n1)]for j in range (m1)]
print("Enter the value of 1st matrix")
for i in range(0,m1):
    for j in range(0,n1):
        print('insert x[',i,',',j,']: ',end=" ")
        x[i][j]=int(input())

print("Enter the value of 2nd  matrix")
for i in range(0,m1):
    for j in range(0,n1):
        print('insert y[',i,',',j,']: ',end=" ")
        y[i][j]=int(input())
print("1.Matrix Addition")
print("2.Matrix Subtraction")
print("3.Matrix Multiplication")
print("4.Matrix Transpose")
print("5.Matrix Trace")
print("Enter The Choice")
ch=int(input())

if(ch==1):
    
    for i in range(m1):
        for j in range(n1):
            result[i][j] = x[i][j] + y[i][j]
    for r in result:
        print(r)
elif(ch==2):
    for i in range(m1):
        for j in range(n1):
            result[i][j] = x[i][j] - y[i][j]
    for r in result:
        print(r)
elif(ch==3):
    
    for i in range(m1):
        for j in range(n1):
            for k in range(n1):
                result[i][j] =result[i][j]+ x[i][k] * y[k][j]
    for r in result:
        print(r)
elif(ch==4):
    result=[[0 for i in range (m1)]for j in range (n1)]
    for i in range(m1):
        for j in range(n1):
            result[j][i] = x[i][j]

    for r in result:
        print(r)

    result=[[0 for i in range (m1)]for j in range (n1)]
    for i in range(m1):
        for j in range(n1):
            result[j][i] = y[i][j]

    for r in result:
        print(r)
elif(ch==5):
    ld=0
    ld1=0
for i in range(0,m1):
    for j in range(0,n1):
        if(i == j):
            ld = ld + x[i][j]
print(ld)


for i in range(0,m1):
    for j in range(0,n1):
        if(i == j):
            ld1= ld1 + y[i][j]
print(ld1)





