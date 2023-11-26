import random
n=random.randint(1,10)

guess=int(input("Enter any number ranges from 1 to 10"))

while n != guess:
    if guess>n:
        print("Too High")
        guess=int(input("Enter number to guess again"))
    elif guess<n:
        print("Too Low")
        guess=int(input("Enter number to guess again"))
    else:
        break
print("you guessed the right number!")