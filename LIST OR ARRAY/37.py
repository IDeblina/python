def Convert(T,Num):
       s=T[0]
       k=0
       for i in range(0,n-1):
           T[i]=T[i+1]
           k=k+1
       T[k]=s
       print(T)
a=[]
n=int(input("Enter range"))
for i in range(n):
    a.append(int(input("Enter nos.")))
Convert(a,n)
