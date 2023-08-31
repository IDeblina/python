a=[]
a1=[]
a2=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter elements")))
print("Initial array--------")
print(a)
for j in range(0,int(ran/2)):
    a1.append(a[j])
for j in range(int(ran/2),ran):
    a2.append(a[j])
print("New arrrays-----")
print(a1)
print(a2)
