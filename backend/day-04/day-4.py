print("Welcome to Rock-Paper-Scissor Game!")
p1 = input("Player1: ")
p2 = input("Player2: ")

if (p1 and p2):
    print("It's a tie!")
elif (p1 == "Rock") and (p2 == "Scissor"):
    print("Player1 Wins!")
elif (p1 == "Scissor") and (p2 == "Paper"):
    print("Player1 Wins!")
elif (p1 == "Paper") and (p2 == "Rock"):
    print("Player1 Wins!")
else: 
    print("Player2 Wins!")