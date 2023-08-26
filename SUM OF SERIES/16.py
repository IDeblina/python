a=2
b=3
s=0
x=2
n=int(input("Enter range"))
for i in range(1,n+1):
    c=a/b
    if(x%2==0):
        s=s+c
    else:
        s=s-c
    a=a+2
    b=b+2
    x=x+1
print(s)
        
        
        
    
