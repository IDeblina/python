n=int(input("Enter the no."))
if(n%2==0 and n%5==0):
    print("Divided by 2 and 5")
elif(n%2==0 and n%5!=0):
    print("Divided by 2 but not 5")
elif(n%5==0 and n%2!=0):
    print("Divided ny 5 but not 2")
else:
    print("Not divided by 5,2")
    
