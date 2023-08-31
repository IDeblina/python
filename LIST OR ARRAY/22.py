import math
a=[]
for i in range(5):
    a.append(int(input("Enter no.")))
print("Perfect Squares are=")
for i in range(5):
    n=math.sqrt(a[i])
    if(n*n==a[i]):
        print(a[i],end=" ")
        
