def Get2From1(a,y):
    odd=[]
    even=[]
    for i in range(y):
        if(i%2==0):
            even.append(a[i])
            
        else:
            odd.append(a[i])
    print(even)
    print(odd)
a=[]
y=int(input("Enter range"))
for i in range(y):
    a.append(int(input("Enter nos.")))
Get2From1(a,y)
