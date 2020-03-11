# demonstrates: comments, print, escape character, string literal
# print a header for the game
print("\n**** Welcome to Rock, Paper, Scissors ****\n")

# demonstrates: comments, print, string literal
# print a header for the game
# print("")
# print("**** Welcome to Rock, Paper, Scissors, lizard, spock ****")
# print("")

# demonstrates: comments, assignment, input, string literal, formatting
# get player 1 input
player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()

# demonstrates: comments, assignment, input, string literal, formatting
# get player 2 input
player2 = raw_input("Player 2, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()

# demonstrates: comments, if..elif..else, equality, blocks/indentation, print
# compare input and output winner
if (player1 == player2):
    # demonstrates: format
    print("Tie, both players chose {}").format(player1)
    # demonstrates: string concatenation
    # print("Tie, both players chose " + player1)
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