a=int(input("Enter a no."))
s=0
while(a>0):
    r=int (a%10)
    s=s*10+r
    a=int (a/10)
print("Reverse=",s)
