n=int(input("Enter range"))
a=1
b=2
print(a,end=" ")
print(b,end=" ")
for i in range(1,n+1):
    c=b*2+a
    print(c,end=" ")
    a=b
    b=c
    
    
    
