def swap(a,ran):
    for i in range(0,int(ran/2)):
        t=a[i]
        a[i]=a[int(ran/2)+i]
        a[int(ran/2)+i]=t
    print(a)

a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
swap(a,ran)
