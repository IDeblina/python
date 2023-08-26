a=int(input("Enter age"))
m=input("Enter marriage status M/U")
g=input("Enter gender X/Y")
if(m=="M" or (m=="U" and g=="X" and a>30) or (m=="U" and g=="Y" and a>25) ):
    print("Insured")
else:
    print("Not insured")
    
