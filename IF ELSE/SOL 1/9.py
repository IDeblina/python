a=int(input("Enter no."))
r=int(a/10)
n=int(a%10)
if((r+n)+(r*n)==a):
    print("Special 2 digit no.")
else:
    print("NOT")
