ran=int(input("Enter number of students."))
name=[]
m=[]
for i in range(ran):
    print("For Student",i+1,"=")
    name.append(str(input("Enter name.")))
    m.append(int(input("Enter marks in CS.")))
for j in range(ran):
    for k in range(ran-1):
        if(m[k]<m[k+1]):
            t=m[k]
            m[k]=m[k+1]
            m[k+1]=t
            t1=name[k]
            name[k]=name[k+1]
            name[k+1]=t1
print("According to Mertit The List is Sorted...")
print("NAME    MARKS")
for i in range(ran):
    print(name[i],"   ",m[i])
