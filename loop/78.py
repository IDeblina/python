s1=s2=s3=0
for i in range(1,6):
    a=int(input("Enter no."))
    if(a<0):
        s1=s1+a
    if(a>0 and a%2==0):
        s2=s2+a
    if(a>0 and a%2!=0):
        s3=s3+a
    if(a==0):
        break;
print("sum of negative numbers=",s1)
print("sum of positive even numbers",s2)
print("sum of positive odd numbers",s3)
    
        
