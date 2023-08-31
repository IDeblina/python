y=10
for i in range(1,6):
    for j in range(1,y+1):
        print(" ",end="")
    y=y-1
    x=1
    for j in range(1,i+1):
        print(x,end=" ")
        x=x+1
    print("")
