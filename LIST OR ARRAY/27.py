a=[]
n=int(input("Enter range="))
for i in range(n):
    a.append(int(input("Enter no.")))
print("Sum of First ans Last digits of Array elements=")
for i in range(n):
    last=a[i]%10
    l=a[i]
    c=0
    while(l>0):
        l=int(l/10)
        c=c+1
    first=int(a[i]/pow(10,c-1))
    print(first+last,end=" ")
    
