def CHANGE(a,ran):
    for i in range(0,ran):
        if(a[i]%7==0):
            a[i]=int(a[i]/7)
        else:
            a[i]=a[i]*3
    print(a)

a=[]
ran=int(input("Enter range="))
for i in range(0,ran):
    a.append(int(input("Enter element.=")))
CHANGE(a,ran)

