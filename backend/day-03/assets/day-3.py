scene1 = input("Man: ""Help me find shelter :< ""(Yes/No): ")
if scene1 == "Yes":
    scene2 = input("Police: Have you seen a strange man?(Yes/No): ")
    if scene2 == "Yes":
        print("WIN!")
    else:
        print("GAME OVER!")
else:
    scene3 = input("*The man attacks you!* Knock him down?(Yes/No): ")
    if scene3 == "Yes":
        print("WIN!")
    else:
        print("GAME OVER!")