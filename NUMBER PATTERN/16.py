x=3
for i in range(1,5):
    for j in range(1,i+1):
        print(" ",end="")
    print(i,end="")
    for k in range(1,x+1):
        print("  ",end="")
    x=x-1
    if(i<4):
        print(i,end="")
    print("")
#--------------------------#
x=1
for i in range(3,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    print(i,end="")
    for k in range(1,x+1):
        print("  ",end="")
    x=x+1
    if(i<4):
        print(i,end="")
    print("")
