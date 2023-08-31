ran=int(input("Enter range="))
a=[]
for i in range(ran):
    a.append(int(input("Enter no.")))
print("Original Array...")
for i in range(int(ran/2)):
    for k in range(int(ran/2)-1):
        if(a[k]>a[k+1]):
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t
for i in range(int(ran/2),ran):
    for k in range(int(ran/2),ran-1):
        if(a[k]<a[k+1]):
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t
print("Sorted Array...")
print(a)
