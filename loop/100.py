def sumdigits(n):
    s=0
    while(n>0):
        r=int(n%10)
        s=s+r
        n=n//10
    return (s)
n=input("Enter a no.")
l=len(n)
n1=int(n)
if(l==15):
    s1=0
    for i in range(15,0,-1):
        r1=int(n1%10)
        if(i%2==0):
            r1=r1*2
        s1=s1+sumdigits(r1)
        n1=n1//10
    if(s1%10==0):
        print("valid IMEI")
    else:
        print("not valid IMEI")
else:
    print("No. should be of 15 digits")
