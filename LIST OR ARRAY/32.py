a=[]
l=int(input("Enter range="))
s=0
for i in range(l):
     a.append(int(input("Enter No.")))
print("Happy Numbers Are=")
for i in range(l):
    n=a[i]
    while(n>9):
        num=n
        s=0
        while(num>0):
           r=num%10
           s=s+r*r
           num=int(num/10)
        n=s

    if(s==1):
        print(a[i],end=" ")
    
