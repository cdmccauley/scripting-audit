# demonstrates: comments, print, escape character, string literal
# print a header for the game
# print("\n****Welcome to Rock, Paper, Scissors****\n")

# demonstrates: comments, print, string literal
# print a header for the game
print("")
print("****Welcome to Rock, Paper, Scissors, lizard, spock****")
print("")

# get player 1 input
player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ")
player1.lower()
# print(player1)

# get player 2 input
player2 = raw_input("Player 2, choose: rock, paper, scissors, lizard, or spock: ")
player2.lower()
# print(player2)

# process input and output winner
if (player1 == player2):
    print("Tie, both players chose " + player1)
elif (player1 == "rock" and player2 == "paper"):
    print("Player 2 wins, paper covers rock.")
elif (player1 == "rock" and player2 == "scissors"):
    print("Player 1 wins, rock smashes scissors.")
elif (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins, paper covers rock.")
elif (player1 == "paper" and player2 == "scissors"):
    print("Player 2 wins, scissors cut paper.")
elif (player1 == "scissors" and player2 == "rock"):
    print("Player 2 wins, rock smashes scissors.")
elif (player1 == "scissors" and player2 == "paper"):
    print("player 1 wins, scissors cut paper.")
else:
    print("Error: Somebody did not select rock, paper, or scissors.")