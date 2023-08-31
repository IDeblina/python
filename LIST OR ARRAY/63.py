def bsearch(arr):
    first=0
    last=len(arr)
    mid=(first+last)//2
    search=int(input('Enter search element:'))
    while(first<=last):
        if(arr[mid]<search):
            first=mid+1
        elif(arr[mid]==search):
            print("Element found at pos %d" %(mid+1))
            break;
        elif(arr[mid]>search):
            last=mid-1
        mid=(first+last)//2
    if(first>last):
        print('Element not Found')

def bsort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(a)
      
arr=[]
for i in range(int(input('Enter range:'))):
    arr.append(int(input('Enter no.')))
bsort(arr)
bsearch(arr)



