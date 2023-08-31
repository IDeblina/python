a=[]
k=0
l=int(input("Enter range"))
for i in range(l):
    a.append(input("Enter name"))
s=input("Enter search value")
for i in range(l):
    if(s==a[i]):
        k=1
if(k==1):
    print("Search found")
else:
    print("Not found")
             
