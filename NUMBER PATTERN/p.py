for i in range(1,6):
    if(i%2==0):
        k=2
    else:
        k=1
    for j in range(1,i+1,k+2):
        print(k,end="")
    print()
