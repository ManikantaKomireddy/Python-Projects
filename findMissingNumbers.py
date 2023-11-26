#finding the missing number in the list
def findMissingNumbers(n):
    numbers=tuple(n)
    l=len(n)
    missingNumbers=[]
    
    for i in range(1,n[-1]):
        if i not in numbers:
            missingNumbers.append(i)
    print(missingNumbers)
    
listOfNumbers=[1,3,5,7,9,11,13,15]
findMissingNumbers(listOfNumbers)