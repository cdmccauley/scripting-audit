# declarations
choices = ["rock", "paper", "scissors", "lizard", "spock"]
playAgain = "Y"

# print a header for the game
print("\n**** Welcome to Rock, Paper, Scissors ****\n")

# play game loop
while playAgain.upper() == "Y":
    # assign default value for validation
    inputOk = False
    # loop until inputOk is True
    while inputOk == False:
        # get player 1 input
        player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()
        if (player1 in choices):
            inputOk = True
        else:
            print("Error: Invalid selection. Try again.")

    # prompt for continuation or termination
    playAgain = raw_input("Enter 'Y' to play again: ")