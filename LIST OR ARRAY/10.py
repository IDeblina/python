a=[1,2,3,4,5,6,7,8,9,10]
k=0
s=int(input("Enter number to search="))
for i in range(10):
    if(s==a[i]):
        k=1
if(k==1):
    print("Seach successfull")
else:
    print("Search unsuccessfull")
    
