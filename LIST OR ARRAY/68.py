r=int(input("Enter number of participants."))
#minimum players=3   maximum players=11-----
if(r<3 or r>11):
    print('INPUT SIZE OUT OF RANGE')
    exit()

  
#created matrix--------------
x=[[0 for i in range(r)]for j in range(5)]

#input taken--------------
for i in range(r):
    print('---PARTICIPANT ',i+1,'---')
    for j in range(5):
        print("Select option for Q.",j+1,end="=")
        x[i][j]=input()
        
#correct answers------------------------     
answers=['D','C','C','A','B']

#scores calculation---------------------
arr=[]
print('---SCORES---')
for i in range(r):
    points=0
    for j in range(5):
        if(x[i][j].upper()==answers[j]):
            points+=1
    print('Participant ',i+1,'=',points)
    arr.append(points)
    
#display----------------------------
print('\n\nHighest Score:\n')
for i in arr:
    if i==max(arr):
        print("Paricipant ",arr.index(i))

