a=[]
p=[]
n=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
for i in range(ran):
    if(a[i]%2==0 and a[i]>0):
        p.append(a[i])
    if(a[i]%2==1 and a[i]<0):
        n.append(a[i])
print("Even Postive Numbers")
print(p)
print("Odd Negative Numbers")
print(n)
