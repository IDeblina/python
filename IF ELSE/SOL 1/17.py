Y=int(input("Enter year:"))
if(Y%4==0 and Y%100!=0 or Y%400==0):
    print("Leap year")
else:
    print("Not Leap year")
