a=1
x=2
y=1
for i in range(1,4):
    for j in range(1,x+1):
        print("  ",end="")
    x=x-1
    for j in range(1,y+1):
        print(a,end=" ")
        a=a+1
    y=y+2
    print("")
    
