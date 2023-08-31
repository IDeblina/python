def check(a,ran):
    l=1
    s=1
    for i in range(ran-1):
        if(a[i]<a[i+1]):
            l=l+1
        if(a[i]>a[i+1]):
            s=s+1
    if(l==ran):
        return 1
    elif(s==ran):
        return -1
    else:
        return 0
a=[]
ran=int(input("Enter range="))
for i in range(ran):
        a.append(int(input("Enter no.")))
x=check(a,ran)
if(x==1):
    print("Ascending Order")
elif(x==-1):
    print("Descending Order")
else:
    print("Not Sorted")
        
