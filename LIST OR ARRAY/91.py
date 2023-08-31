a=[]
a1=[]
ran=int(input("Enter range"))
for i in range(ran):
    a.append(int(input("Enter no.")))
for i in range(0,ran,1):
    if(a[i]==a[0]):
        t=a[1]*a[0]
    elif(a[i]==a[ran-1]):
        t=a[ran-1]*a[ran-2]
    else:
        t=a[i-1]*a[i+1]
    a1.append(t)
    print("")
print("The new array is=",end="")
print(a1)


