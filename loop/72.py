c=0
for i in range(1,6):
    n=int(input("Enter no."))
    if(i>1 and n==p):
        c=c+1
    else:
        p=n
if(c==4):
    print("All numbers are same")
else:
    print("All numbers are not same")
    
    
               
