con=['Germany','Nepal','Japan','Canada','Iraq','Sri lanka','Brazil','Australia','India','South America']
city=['Berlin','Katmandu','Tokyo','Montreal','Baghdad','Colombo','Brazilia','Perth','Dehli','Pretoria']
n=str(input("ENTER NAME OF A COUNTRY="))

for i in range(10):
      k=0
      if(n==con[i]):
          k=1
          print("The corresponding city is=",city[i])
          break
if(k==0):
    print("Country you entered is not the List")

      
    
