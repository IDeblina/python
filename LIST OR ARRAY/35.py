r=int(input("Enter row"))
c=int(input("Enter collumn"))
x=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter element",(i+1,j+1))
        x[i][j]=int(input())
print("Original Matrix..")
print(x)
print("Transpose...")
for i in range(r):
    for j in range(c):
        print(x[j][i],end=" ")
    print("")
