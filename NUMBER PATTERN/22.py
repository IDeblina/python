a=4
b=1
for i in range(1,5):
    for j in range(1,5):
        if(j>a):
            print("*",end="")
        else:
            print(j,end="")
    a=a-1
    #=======================#
    x=4
    for j in range(1,5):
        if(j<b):
            print("*",end="")
            x=x-1
        else:
            print(x,end="")
            x=x-1
    b=b+1
    print("")
