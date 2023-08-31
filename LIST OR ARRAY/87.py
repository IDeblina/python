def write(c1,c2,ran):
    k=1
    for i in range(ran):
        if(c1[i]>c2[i]):
            for j in range(k):
                print(c1[i],end=" ")
        else:
            for j in range(k):
                print(c2[i],end=" ")
        k=k+1
        print("")
c1=[]
c2=[]
ran=int(input("Enter range"))
print("Enter 1st char array..")
for i in range(ran):
    c1.append(str(input("Enter.")))
print("Enter 2nd char array..")
for i in range(ran):
    c2.append(str(input("Enter.")))    
write(c1,c2,ran)
