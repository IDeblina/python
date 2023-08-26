n=int(input("Enter no."))
k=0
for i in range(0,n+1):
    if(i*(i+1)==n):
        k=1
if(k==1):
    print("Pronic no.")
else:
    print("not pronic no.")
        
