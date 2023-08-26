import math
a=int(input("Enter no"))
b=int(input("Enter no"))
c=int(input("Enter no"))
d=(b*b)-4*a*c
if(d>=0):
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print ("r1=",r1)
    print ("r2=",r2)
else:
    print("Roots are imaginary")
