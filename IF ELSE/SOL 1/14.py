U=int(input("Enter units"))
if(U<=100):
    B=U*0.40
elif(U<=200):
    B=(U*0.40)+(U-100)*0.50
else:
    B=(100*0.40)+(100*0.50)+(U-200)*0.60
print(B)
