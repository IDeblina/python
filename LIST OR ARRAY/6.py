a=[]
n=int(input("Enter range"))
for i in range(n):
    a.append(int(input("Enter temps.")))
for i in range(n):
    p=a[i]
    c=5/9*(p-32)
    print(c)
