n=int(input("Enter range"))
k=0
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(1,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
s=int(input("Enter no.to be searched"))
a=0
b=1
for i in range(1,n):
    c=a+b
    if(c==s):
        k=1
    a=b
    b=c
if(k==1):
    print("Present in series")
else:
    print("not present")
