N=int(input("Enter rows."))
M=int(input("Enter collumns."))
x=[[0 for i in range(N)]for j in range(M)]
for i in range(N):
    for j in range(M):
        print("Enter element ",(i+1,j+1))
        x[i][j]=int(input())
s=0
s1=0
for j in range(M):
    s=s+x[0][j]
print("Sum of top row=",s)
for j in range(M):
    s1=s1+x[N-1][j]
print("Sum of Bottom row=",s1)
