a=[17,42,42,7,24,24,17,54,17]
l=0
for i in range(8):
    if(a[i]==a[i+1]):
        l=l+1
print("Number of Clumps in the array=",l)
