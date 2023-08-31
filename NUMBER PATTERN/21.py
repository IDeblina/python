y=8
a=1
for i in range(1,6):
    x=1
    for j in range(1,i+1):
        print(x,end="")
        x=x+1
    for j in range(1,y+1):
        print(" ",end="")
    y=y-2
    for j in range(a,0,-1):
        print(j,end="")
    a=a+1
    print("")
