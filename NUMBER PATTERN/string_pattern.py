n=input("Enter name:")
l=len(n)
for i in range(l+1,0,-1):
    for j in range(0,i-1):
        print(n[j],end='')
    print()
