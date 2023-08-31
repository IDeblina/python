arr=[]
for i in range(int(input('Enter range:'))):
    arr.append(int(input('Enter element:')))
temp=sorted(arr)
count=0
for i in range(len(temp)-1):
    if(temp[i]!=temp[i+1]-1):
        count+=1
if(count==0):
    print('The appearence of elements in the array are consecutive.')
else:
    print('The appearence of elements in the array are NOT consecutive.')
