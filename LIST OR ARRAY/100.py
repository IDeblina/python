arr=[1,3,6,21,4,9,12,3,16,10]
m,n=0,4
print('The contagious subarray of length 4 and their maximum value are:')
while(n<=len(arr)):
    print(*arr[m:n],'-->',max(arr[m:n]))
    m+=1
    n+=1
