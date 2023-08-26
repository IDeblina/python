a=int(input("Enter no."))
for i in range(1,10):
    n=a
    while(n>0):
        r=int(n%10)
        if(r==i):
            print(i)
            exit()
        n=int(n/10)
        
