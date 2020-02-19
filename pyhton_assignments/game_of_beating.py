
player1 = input("Player 1, enter your choice (R/P/S): ")
player2 = input("Player 2, enter your choice (R/P/S): ")

if ((player1 == "P" and player2 == "R") or (player1 == "R" and player2 == "S") or (player1 == "S" and player2 == "P")):
    print("Player 1 won!")
elif ((player2 == "P" and player1 == "R") or (player2 == "R" and player1 == "S") or (player2 == "S" and player1 == "P")):
    print("Player 2 won!")

else:
    print("It's a tie!")
