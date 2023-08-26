import math
a=math.sin(30)
b=math.cos(30)
c=math.tan(30)
if(a<b and a<c):
    print("Sin 30 is lowest")
elif(b<a and b<c):
    print("Cos 30 is lowest")
else:
    print("Tan 30 is lowest")
    
