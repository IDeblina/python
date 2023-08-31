def transfer(a,n,b):
    for i in range(n):
        if(i%2==1):
            t=a[i]
            a[i]=b[i]
            b[i]=t
    print("New 1st array===")
    print(a)
    print("New 2nd array===")
    print(b)
a=[]
b=[]
n=int(input("Enter range="))
print("Enter elements of 1st array===")
for i in range(n):
    a.append(int(input("Enter no.")))
print("Enter elements of 2nd array===")
for i in range(n):
    b.append(int(input("Enter no.")))
transfer(a,n,b)
