a=int(input("Enter Maths no."))
b=int(input("Enter Sci no."))
c=int(input("Enter SST no."))
d=int(input("Enter Beng. no."))
e=int(input("Enter Comp no."))
p=(a+b+c+d+e)/5
if(p>=80):
    print("E+")
elif(p>=70 and p<80):
    print("E")
elif(p>=60 and p<70):
    print("A+")
elif(p>=50 and p<60):
    print("A")
elif(p>=40 and p<50):
    print("B")
else:
    print("Fail")
