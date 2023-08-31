def Get1From2(a,b,f,s):
    p=f+s
    al=[]
    j=k=0
    for i in range(p):
        if(i%2==0):
            al.append(a[j])
            j=j+1
        else:
            al.append(b[k])
            k=k+1
    print(al)
    
a=[]
b=[]
f=int(input("Enter range"))
s=int(input("Enter range"))
for i in range(f):
    a.append(int(input("Enter nos.")))
for i in range(s):
    b.append(int(input("Enter nos.")))
Get1From2(a,b,f,s)
