n=int(input("Enter no."))
s=0
m=1
t=n
while(n>0):
    r=int(n%10)
    s=s+r
    m=m*r
    n=int(n/10)
if(s*m==t):
    print("Special no.")
else:
    print("not Special no.")
