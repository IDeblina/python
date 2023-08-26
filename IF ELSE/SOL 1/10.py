t=int(input("Enter temp"))
if(t<=0):
    print("very cold")
elif(0<t and t<=10):
    print("cold")
elif(10<t and t<=20):
    print("cool out")
elif(20<t and t<=30):
    print("Warm")
else:
    print("Hot")
