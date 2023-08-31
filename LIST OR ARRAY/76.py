name=[]
phy=[]
ch=[]
math=[]
t=[]
avg=[]
ran=int(input("Enter Number of Students"))
for i in range(ran):
    print("For Student",i+1)
    name.append(str(input("Enter name")))
    phy.append(int(input("Enter marks in physics")))
    ch.append(int(input("Enter marks in chemistry")))
    math.append(int(input("Enter marks in maths")))
s=0
for i in range(ran):
    s=math[i]+phy[i]+ch[i]
    t.append(s)
    avg.append(s/3)
print("List of Data......")
print("Name of student     Phy     Chem     Math     Total     Avg")
for i  in range(ran):
    print(name[i],"      ",phy[i],"      ",ch[i],"      ",math[i],"      ",t[i],"     ",avg[i])
