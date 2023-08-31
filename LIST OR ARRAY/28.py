a=[]
s=0

n=int(input("Enter range="))
for i in range(n):
    a.append(int(input("Enter No.")))
print("Flappy Numbers Are=")
for i in range(n):
    l=a[i]
    s=0
    while(l>0):
        r=l%10
        s=s+r
        l=int(l/10)
    b=a[i]%10
    c=int(a[i]/10)
    d=c%10
    if(s==36 and b*d==32):
        print(a[i],end=" ")
