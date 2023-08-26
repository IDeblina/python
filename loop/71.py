n=int(input("Enter no."))
l=p=0
last=int(n%10)
while(n>0):
    r=int(n%10)
    if(last==r):
        p=p+1
    n=int(n/10)
    l=l+1
if(l==p):
    print("digits in it are same")
else:
    print("digits in it are not same")
