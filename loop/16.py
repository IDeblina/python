a=int(input("Enter a no."))
s=0
for i in range(1,a):
    if(a%i==0):
        s=s+i
if(s==a):
    print("Perfect no.")
else:
    print("not Perfect no.")
    
