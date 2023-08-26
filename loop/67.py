n=int(input("Enter no."))
s=l=0
while(n>0):
    r=int(n%10)
    s=s+r
    n=int(n/10)
    l=l+1
print("Avg.=",s/l)
    
