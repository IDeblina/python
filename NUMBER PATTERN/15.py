x=5
for i in range(1,6):
    for k in range(1,x+1):
        print("  ",end="")
    x=x-1
    y=1
    for j in range(1,i+1):
        print(y,end=" ")
        y=y+1
    if(i>1):
        for j in range(y-2,0,-1):
            print(j,end=" ")
    print("")
        
