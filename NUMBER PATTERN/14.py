x=5
y=1
print(" ",end="")
for i in range(1,5):
    for j in range(1,x+1):
        print(" ",end="")
    print(i,end=" ")
    for k in range(1,y+1):
        print(" ",end="")
    if(i>1):
        print(i,end=" ")
    
    x=x-1
    y=y+2
    print("")
    print("")
#------------------------#
x=1
y=4
for i in range(3,0,-1):
    print(" ",end=" ")
    for j in range(1,x+1):
        print(" ",end="")
    x=x+1
    print(i,end=" ")
    for k in range(1,y+1):
        print(" ",end="")
    y=y-2
    if(i>1):
        print(i,end=" ")
    print("")
    print("")
    
