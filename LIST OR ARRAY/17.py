a=[]
s=0
for i in range(0,5):
    a.append(int(input("Enter number")))
maximum=a[0]
minimum=a[0]
for i in range(0,5):
    if(maximum<a[i]):
        maximum=a[i]
    if(minimum>a[i]):
        minimum=a[i]
    s=s+a[i]


print("MAXIMUM IS=",maximum)
print("MINIMUM IS=",minimum)
print("SUM OF NUMBERS IS=",s)
