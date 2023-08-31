def merge(a,b,r):
    c=[]
    for i in range(r):
        c.append(2*a[i]+3*b[i])
    print(c)
        
a=[]
b=[]
ran=int(input("Enter range="))
print("Enter elements for 1st array...")
for i in range(ran):
    a.append(int(input("Enter element.")))
print("Enter elements for 2st array...")
for i in range(ran):
    b.append(int(input("Enter element.")))
merge(a,b,ran)
