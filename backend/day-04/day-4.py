print("Welcome to Rock-Paper-Scissor Game!")
p1 = input("Player1: ")
p2 = input("Player2: ")

if p1 == p2:
    print("It's a tie!")
elif (p1 == "Rock" and p2 == "Scissor") or (p1 == "Scissor" and p2 == "Paper") or (p1 == "Paper" and p2 == "Rock"):
    print("Player1 Wins!")
else: 
    print("Player2 Wins!")