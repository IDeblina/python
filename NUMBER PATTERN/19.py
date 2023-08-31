a=1
b=4
for i in range(1,5):
    for j in range(1,5):
        if(j==a):
            print("*",end="")
        else:
            print(0,end="")
    a=a+1
    #========left side=======#
    print("*",end="")
    #======right side========#
    for j in range(1,5):
        if(j==b):
            print("*",end="")
        else:
            print(0,end="")
    b=b-1
    print("")
        
