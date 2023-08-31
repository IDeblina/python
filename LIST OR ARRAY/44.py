def revert(a,r):
    print("Original Array=")
    print(a)
    b=[]
    for i in range(r-1,-1,-1):
        b.append(a[i])
    print(b)


a=[]
ran=int(input("Enter  range="))
for i in range(0,ran):
    a.append(int(input("Enter elements=")))

revert(a,ran)
    
