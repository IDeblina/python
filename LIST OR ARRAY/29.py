##linear search method
a=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter a number to search"))
s=0
for i in range(10):
    if(n==a[i]):
        s=1
if(s==1):
    print("Search Successful")
else:
    print("Search unsuccessful")
