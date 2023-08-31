def oddeven(s,ran):
    print("ORIGINAL ARRAY=",end="")
    for i in range(ran):
        print(a[i],end=" ")
    for i in range(ran):
        if(a[i]%2==0):
            a[i]=a[i]+10
        else:
            a[i]=a[i]+5
    print("")
    print("SORTED ARRAY=",end="")
    for i in range(ran):
        print(a[i],end=" ")


a=[50,11,19,24,28]
oddeven(a,5)
