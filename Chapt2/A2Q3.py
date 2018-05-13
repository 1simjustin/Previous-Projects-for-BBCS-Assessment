p1 = "Player One wins."
p2 = "Player Two wins."
tie = "Draw."
player1 = input("P1 Rock, Paper, Scissors: ")
player2 = input("P2 Rock, Paper, Scissors: ")
if player1 == player2:
    print(tie)
elif (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (player1 == "S" and player2 == "P"):
    print(p1)
else:
    print(p2)
