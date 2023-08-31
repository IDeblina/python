a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter no.")))
k=1
x=0
for i in range(ran):
    if(a[i]!=a[ran-k]):
        x=x+1
    k=k+1
if(x>0):
    print("Not same")
else:
    print("Same")
