arr=[17,42,19,7,27,24,17,54,73]
span=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i]==arr[j]):
            span.append(j-i)
print('Maximum span between the same values in the array is:',max(span)+1)
