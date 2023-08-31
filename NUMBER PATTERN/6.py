for i in range(1,5):
    for j in range(i,5):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()