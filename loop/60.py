n1=int(input("Enter no."))
for i in range(9,0,-1):
    n=n1
    while(n>0):
        r=int(n%10)
        if(r==i):
            print (i,end=" ")
        n=int(n/10)
    
