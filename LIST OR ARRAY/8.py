a=[]
l=int(input("Enter range."))
for i in range(l):
    a.append(int(input("Enter value")))
for i in range(l):
    p=a[i]
    c=0
    for j in range(1,p+1):
        if(p%j==0):
            c=c+1
    if(c==2):
        print("Prime=",a[i])
    else:
        print("Not prime=",a[i])
    
