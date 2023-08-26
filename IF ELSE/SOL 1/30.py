w=int(input("Enter weight"))
if(w<=10):
    c=w*20
elif(w<=30):
    c=w*10
elif(w<=50):
    c=w*8
elif(w>50):
    c=w*5
print ("charge=",c)    
