# Caluculating Execution time of a python program

from time import time

start=time()

n=int(input("Enter a Number"))

if n%2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")

end=time()

execution_time=end-start

print(execution_time)