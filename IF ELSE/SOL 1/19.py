a=int(input("Enter 1st side"))
b=int(input("Enter 2nd side"))
c=int(input("Enter 3rd side"))
if(a==b and b==c and c==a):
    print("Equilateral Trinagle")
elif(a==b or b==c or c==a):
    print("Isosceles Trinagle")
else:
    print("Scalene Trinagle")
