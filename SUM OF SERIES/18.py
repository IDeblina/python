a1=3
s=0
n=int(input("Enter range"))
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+(a1/f)
print(s)
        
