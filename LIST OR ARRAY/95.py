a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
s1=s2=0
for i in range(int(ran/2)):
    s1=s1+a[i]
for i in range(int(ran/2),ran):
    s2=s2+a[i]
if(s1==s2):
    print("Sum of both side is equal")
else:
    print("Not equal")
    
