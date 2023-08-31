a=[1,2,3,4,5,6,7,8,9,10] #monica process
pos=int(input("Enter the position where you want to delete="))
for i in range(pos,9):
    a[i]=a[i+1]
print("New Array=")
for i in range(9):
    print(a[i],end=" ")
