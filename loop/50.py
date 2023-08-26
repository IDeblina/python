a=0
b=0
c=1
k=0
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
for i in range(1,11):
    d=a+b+c
    print(d,end=" ")
    a=b
    b=c
    c=d
s=int(input("Enter no to be searched"))
a=0
b=0
c=1
for i in range(1,11):
    d=a+b+c
    if(d==s):
        k=1
    a=b
    b=c
    c=d
if(k==1):
    print("No. is present")
else:
    print("No.not present")
