unit=["","One","Two","Three","Four","Five","Six","seven","Eight","Nine"]
ten=["","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
t=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
n=int(input("Enter no."))
if(n<1 or n>9999):
    print("Out of range")
else:
    th=int(n/1000)
    h=int(int(n/100)%10)
    t1=int(int(n/10)%10)
    u=int(n%10)
    if(th!=0):
        print(unit[th],' Thousand ',end=" ")
    if(h!=0):
        print(unit[h],' Hundred ',end=" ")
    if((t1!=0 or u!=0) and (th!=0 or h!=0)):
        print('and',end=" ")
    if(t1==1):
        print(ten[u+1],end=" ")
    else:
        print(' ',t[t1],' ',unit[u])
