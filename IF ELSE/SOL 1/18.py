a=int(input("Enter no."))
b=int(input("Enter no."))
c=int(input("Enter no."))
if(a>b and a>c):
    print ("greatest=",a)
elif(b>a and b>c):
    print("greatest=",b)
elif(c>a and c>b):
    print("greatest=",c)
elif(a==b and b==c and c==a):
    print("They are equal")
else:
    print("Unequal")
