x=7
for i in range(1,6):
    y=1
    for j in range(1,x):
        print(" ",end="")
    for k in range(1,i+1):
        print(y,end=" ")
        y=y+1
    x=x-1
    print("")
