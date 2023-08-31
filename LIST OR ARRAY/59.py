r=int(input("Enter r"))
c=int(input("Enter c"))
x=[[0 for i in range(r)]for j in range(c)]
for i in range(r):
    for j in range(c):
        print('insert x[',i,',',j,']:',end="")
        x[i][j]=int(input())
for i in range(r):
    for j in range(c):
        if(i==0 or i==r-1 or j==0 or j==c-1):
            print(x[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")
        
