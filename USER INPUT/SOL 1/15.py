a = int(input("Enter the apothem length of Pentagonal pyramid:"))
b = int(input("Enter the base of Pentagonal pyramid:"))
s = int(input("Enter the slant height of Pentagonal pyramid:"))
h = int(input("Enter the height of Pentagonal pyramid:"))
B = float((5*a*b)/2)
S = float((5*a*b)/2)+((5*b*s)/2)
V = float((5*a*b*h)/6)
print("Base area =",B)
print("Surface area=",S)
print("Volume=",V)
