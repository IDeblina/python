arr=[]
for i in range(int(input('Enter No. of Students:'))):
    arr.append(int(input('Enter Marks of students')))
#selection sort
for i in range(len(arr)-1):
    smallest=i
    for k in range(i+1,len(arr)):
        if(arr[smallest]<arr[k]):
            smallest=k
    if(i!=smallest):
        temp=arr[i]
        arr[i]=arr[smallest]
        arr[smallest]=temp

print('Sorted list is',arr)
print('Highest Marks is:',arr[0])
print('Lowest Marks is :',arr[len(arr)-1])
    
