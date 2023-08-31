def mix(a,b,n):
    c=[]
    for i in a:
        if i%2==0:c.append(i)
    for i in b:
        if i%2==0:c.append(i)
    for i in b[::-1]:
        if i%2!=0:c.append(i)
    for i in a[::-1]:
        if i%2!=0:c.append(i)
    print(c)  
x=[]
y=[]
n,m=int(input('Enter 1st array range')),int(input('Enter 2nd array range'))
for i in range(n):
    x.append(int(input('Enter 1st array elements')))
for i in range(m):
    y.append(int(input('Enter 2nd array elements')))
mix(x,y,n+m)
