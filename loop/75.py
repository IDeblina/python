import math
n=int(input("Enter no."))
length=len(str(n))
c=n*n*n
p=int(c%int(math.pow(10,length)))
if(p==n):
    print("Trimorphic no.")
else:
    print("not Trimorphic no.")
