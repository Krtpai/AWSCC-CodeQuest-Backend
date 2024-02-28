import random

print("Welcome to Rock-Paper-Scissors!")
p1 = input("Pick your choice: ").lower()
options = ["rock", "paper", "scissors"]
p2 = random.choice(options)
print("Player 2 chose:", p2)

if p1 == p2:
    print("It's a tie!")
elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")