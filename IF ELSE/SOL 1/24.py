a=int(input("Enter price"))
if(a<=2000):
    D=a*0.05
elif(a>=2001 and a<=5000):
    D=a*0.25
elif(a>=5001 and a<=10000):
    D=a*0.35
elif(a>10000):
    D=a*0.50
amt=a-D
print("Price",a)
print("Discount",D)
print("Amount",amt)
    
    
