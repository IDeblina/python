c=[]
cap=[]
l=int(input("Enter range"))
for i in range(l):
    c.append(input("Enter country names"))
    cap.append(input("Enter capital names"))
for i in range(l):
    print(c[i],' ',cap[i])
