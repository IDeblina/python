a=int(input("Enter a's value:"))
n=int(input("Enter range:"))
s=0
b=2
for i in range(1,n+1):
    s=s+(a/b)
    b=b*2
print(s)
