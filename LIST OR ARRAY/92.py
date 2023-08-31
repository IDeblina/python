arr=[5,8,1,4,2,9,3,7,6]
arr.sort()
res=[]
i,k,j=0,0,-1
while(i<len(arr)):
    if i%2==0:
        res.append(arr[k])
        k+=1
    else:
        res.append(arr[j])
        j-=1
    i+=1
print(res)
