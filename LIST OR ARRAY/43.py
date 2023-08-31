def swap(a,ran):
    print("Original Array=")
    print(a)
    if(ran%2!=0):
        ran=ran-1
    for i in range(0,ran):
        if(i%2==0):
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
            i=i+1
        else:
            i=i+1
    print("New array=")
    print(a)


a=[]
ran=int(input("Enter range="))

for i in range(0,ran):
    a.append(int(input("Enter element=")))
swap(a,ran)
    
