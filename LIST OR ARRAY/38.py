def SWAP2CHANGE(p,N):
    i=0
    while(i<N-1):
        if(p[i]%10==0):
            t=p[i]
            p[i]=p[i+1]
            p[i+1]=t
            i=i+1
        i=i+1
    print(p)
a=[]
n=int(input("Enter range"))
for i in range(n):
    a.append(int(input("Enter nos.")))
SWAP2CHANGE(a,n)
