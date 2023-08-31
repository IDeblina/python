c=1
for i in range(1,5):
    o=c
    for k in range(1,i+1):
        print(c,end="")
        c=c+1
    for j in range(c-2,o-1,-1):
        print(j,end="")
    print("")
