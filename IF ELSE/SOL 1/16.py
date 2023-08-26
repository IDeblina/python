M=int(input("Enter Maths no."))
P=int(input("Enter Physics no."))
C=int(input("Enter Chemistry no."))
if(M>=60 and P>=50 and C>=40 and M+P+C>=200 or M+P>=150):
    print("Eligible")
else:
    print("Not eligible")
