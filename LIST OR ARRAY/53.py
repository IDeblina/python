a=[123456789,1401601499,235656,98373737373,9876543214]
s=0
print("Legal ISBN Numbers are=")
print(" ")
for i in range(5):
    x=a[i]
    y=a[i]
    l=0
    while(x>0):
        x=int(x/10)
        l=l+1
    if(l==10):
        for m in range(10,0,-1):
            r=y%10
            s=s+r*m
            y=int(y/10)

        if(s%11==0):
            print(a[i],"=Legal ISBN")
        else:
            print(a[i],"=Illegal ISBN")
    else:
        print(a[i],"=Number must be 10 digit")
            
            
