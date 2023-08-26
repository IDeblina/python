a=int(input("Enter a's value:"))
n=int(input("Enter range:"))
s=0
b=2
x=1
j=2
for i in range(1,n+1):
    if(j%2==0):
        s=s+x
        x=x+2
    else:
        s=s-(a/b)
        b=b+2
    j=j+1
print(s)
