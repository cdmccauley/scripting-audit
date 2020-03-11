# demonstrates: lists
# declarations
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# print a header for the game
print("\n**** Welcome to Rock, Paper, Scissors ****\n")

# demonstrates: for...in..range, while loop, nested loop, formatting
# get player 1 input
for i in range(1, 5):
    inputOk = False
    while inputOk == False:
        player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()
        # demonstrates: in keyword
        if (player1 in choices):
            inputOk = True
        else:
            print("Error: invalid selection. Try again.")

# demonstrates: for...in..range, formatting
# get player 2 input
for i in range(1, 5):
    inputOk = False
    while inputOk == False:
        player2 = raw_input("Player 2, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()
        # demonstrates: in keyword
        if (player2 in choices):
            inputOk = True
        else:
            print("Error: invalid selection. Try again.")

# compare input and output winner
if (player1 == player2):
    print("Tie, both players chose {}").format(player1)
elif (player1 == "rock" and player2 == "paper"):
    print("Player 2 wins, paper covers rock.")
elif (player1 == "rock" and player2 == "scissors"):
    print("Player 1 wins, rock smashes scissors.")
elif (player1 == "rock" and player2 == "lizard"):
    print("Player 1 wins, rock smashes lizard")
elif (player1 == "rock" and player2 == "spock"):
    print("Player 2 wins, Spock vaporizes rock.")
elif (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins, paper covers rock.")
elif (player1 == "paper" and player2 == "scissors"):
    print("Player 2 wins, scissors cut paper.")
elif (player1 == "paper" and player2 == "lizard"):
    print("Player 2 wins, lizard eats paper.")
elif (player1 == "paper" and player2 == "spock"):
    print("Player 1 wins, paper disproves Spock")
elif (player1 == "scissors" and player2 == "rock"):
    print("Player 2 wins, rock smashes scissors.")
elif (player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins, scissors cut paper.")
elif (player1 == "scissors" and player2 == "lizard"):
    print("Player 1 wins, scissors decapitate lizard.")
elif (player1 == "scissors" and player2 == "spock"):
    print("Player 2 wins, Spock smashes scissors.")
elif (player1 == "lizard" and player2 == "rock"):
    print("Player 2 wins, rock smashes lizard.")
elif (player1 == "lizard" and player2 == "paper"):
    print("Player 1 wins, lizard eats paper.")
elif (player1 == "lizard" and player2 == "scissors"):
    print("Player 2 wins, scissors decapitate lizard.")
elif (player1 == "lizard" and player2 == "spock"):
    print("Player 1 wins, lizard poisons Spock.")
elif (player1 == "spock" and player2 == "rock"):
    print("Player 1 wins, Spock vaporizes rock.")
elif (player1 == "spock" and player2 == "paper"):
    print("Player 2 wins, paper disproves Spock.")
elif (player1 == "spock" and player2 == "scissors"):
    print("Player 1 wins, Spock smashes scissors.")
elif (player1 == "spock" and player2 == "lizard"):
    print("Player 2 wins, lizard poisons Spock.")
else:
    print("Error: Somebody did not select rock, paper, or scissors.")