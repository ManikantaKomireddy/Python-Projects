#Rock, Paper,Scissors game
import random

player1=random.choice(["Rock","Paper","Scissors"])
player2=random.choice(["Rock","Paper","Scissors"])

print(f"Player1 selection is {player1} and Player2 selction is {player2}")

if player1 == "Rock" and player2 == "Paper":
    print("Player2 won the game")
elif player1 == "Paper" and player2 == "Scissors":
    print("Player2 won the game")
elif player1 == "Scissors" and player2 == "Rock":
    print("Player2 won the game")
elif player1 == player2:
    print("Tie")
else:
    print("Player1 won the game")