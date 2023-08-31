a=[]
for i in range(4):
    a.append(int(input("Enter no.")))
b=[]
print("OPERATORS==* + - /")
for i in range(3):
    b.append(str(input("Input Operators")))
s=a[0]
for i in range(3):
    if (b[i]=='/'):
        s=s/a[i+1]
    if (b[i]=='-'):
        s=s-a[i+1]
    if (b[i]=='*'):
        s=s*a[i+1]
    if (b[i]=='+'):
        s=s+a[i+1]
print("Answer will be ",s)
