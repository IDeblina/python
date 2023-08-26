n=int(input("Enter no."))
s=str(n)
n1=s[::-1]
c=int(n1)
d=len(s)
a=[]
for i in range(d-1,-1,-1):
    p=int(c%10)
    a.append(p)
    c=c//10
i=d
s1=0
while(s1<n):
    s1=0
    for j in range(1,d+1):
        s1=s1+a[i-j]
    a.append(s1)
    i=i+1
if(s1==n):
    print("Keith no.")
else:
    print("Not Keith no.")
    
