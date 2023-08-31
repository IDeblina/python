x=7
a=1
for i in range(1,6):
    
    for j in range(1,x+1):
        print("",end="  ")
    for j in range(1,i+1):
        print(a,end="   ")
        a=a+1
    x=x-2
    print("")
    
