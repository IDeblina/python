n=int(input("Enter no."))
s1=0
for i in range(1,n+1):
    p=i
    a=p*p
    s=0
    while(a>0):
        r=int(a%10)
        s=s*10+r
        a=int(a/10)
    s1=s1+s
print(s1)
