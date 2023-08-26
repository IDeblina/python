a=int(input("Enter a no."))
b=int(input("Enter a no."))
p=a*b
for i in range(1,p):
    if(a%i==0 and b%i==0):
        HCF=i
LCM=p/HCF
print("HCF=",HCF)
print ("LCM=",LCM)
