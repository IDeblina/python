import math
n=int(input("Enter no."))
b=s1=0
s=1
while(n>0):
    r=int(n%10)
    s=s+r*math.pow(8,b)
    n=n//10
    b=b+1
print(s)
n=s
b1=1
while(n>0):
    r=int(n%2)
    s1=s1+b1*r
    n=n//2
    b1=b1*10
print("Octal to bin=",s1)
    
