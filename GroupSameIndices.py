#Grouping the elements of same indices in a list
list1=[[1,2,3],[10,20,30],[100,200,300]] 
outputList=[]
n=len(list1)

for i in range(n):
    outputList.append([])
    for j in range(n):
        outputList[i].append(list1[j][i])
    
a,b,c=outputList[0],outputList[1],outputList[2]
print(a,b,c)
    
        