M=int(input("Enter Maths no."))
P=int(input("Enter Physics no."))
E=int(input("Enter English no."))
if(E+M+S>=80):
    print("Pure Sci.")
elif(E+S>=80 and M>=60):
    print("Bio Sci.")
elif(E+M+S>=60):
    print("Commerce")
