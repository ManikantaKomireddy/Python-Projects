#Program calculates the mean meadian for the list of numbers

def mean(list):
    mean=sum(list)/len(list)
    print(f"The mean value is {mean}")
    
def median(list):
    if len(list)%2 == 0:
        val1=list[len(list)//2]
        val2=list[len(list)//2-1]
        median=(val1+val2)/2
        print(f"The medain is {median}")
    else:
        median=list[len(list)//2]
        print(f"The medain is {median}")
    


list=[]
n=int(input("Enter the number of elements you want to take from the user to calculate mean and median"))

for i in range(0,n):
    ele=int(input("Enter a number"))
    list.append(ele)
mean(list)
median(list)
