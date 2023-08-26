n=int(input("Enter no."))
for i in range(9,0,-1):
    a=n
    while(a>0):
        r=int(a%10)
        if(r==i):
            print(i)
            exit()
        a=int(a/10)
