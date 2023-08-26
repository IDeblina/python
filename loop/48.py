n=int(input("Enter no."))
for i in range(1,10):
    p=n
    while(p>0):
        r=int(p%10)
        if(r==i):
            print(i,end=" ")
        p=p//10
        
