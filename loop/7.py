n=int(input("Enter no."))
t=n
s=0
a=n*n
while(a>0):
    r=int(a%10)
    s=s+r
    a=int(a/10)
if(s==t):
    print("Neon no.")
else:
    print("not Neon no.")
