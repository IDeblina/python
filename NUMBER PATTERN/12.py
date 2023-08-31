a=0
b=1
print("1 ")
for i in range(1,5):
    for j in range(1,i+2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    print("")
