def chalo(a,r):
    m=n=o=p=q=0
    for i in range(r):
        if(a[i]>0):
            m=m+1
        if(a[i]<0):
            n=n+1
        if(a[i]==0):
            o=o+1
        if(a[i]%2==0):
            p=p+1
        if(a[i]%2!=0):
            q=q+1
    print("Positive numbers=",m)
    print("Negative numbers=",n)
    print("Zeros=",o)
    print("Even numbers=",p)
    print("Odd numbers=",q)
a=[]
ran=int(input("Enter range="))
for i in range(ran):
    a.append(int(input("Enter element=")))

chalo(a,ran)
