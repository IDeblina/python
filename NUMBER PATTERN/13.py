n=39714
print("P=",n)
l=5
for i in range(1,6):
    j=pow(10,l)
    k=n%j
    print(k,end=" ")
    l=l-1
    print("")
