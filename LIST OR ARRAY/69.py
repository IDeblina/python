a=[]
print("Array of Factorials=")
for i in range(1,11):
    r=1
    for j in range(1,i+1):
        r=r*j
    a.append(r)
print(a)
