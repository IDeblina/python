a=0
b=1
c=1
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
for i in range(1,11):
    d=a+b+c
    print(d,end=" ")
    a=b
    b=c
    c=d
