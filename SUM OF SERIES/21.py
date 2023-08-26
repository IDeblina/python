a=int(input("Enter a's value:"))
n=int(input("Enter range:"))
s=0
b=2
k=2
for i in range(1,n+1):
    f=1
    for j in range(1,b+1):
        f=f*j
    if(k%2==0):
        s=s+(a/f)
    else:
        s=s-(a/f)
    b=b+1
    k=k+1
print(s)
