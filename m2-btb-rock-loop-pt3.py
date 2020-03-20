# imports
import random

# declarations
# demonstrates: dictionaries
choices = {
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "lizard",
    5: "spock"
}
playAgain = "Y"

# functions
def getComputerInput():
    return choices.get(random.randint(1,5))

# print a header for the game
print("\n**** Welcome to Rock, Paper, Scissors ****\n")

# play game loop
while playAgain.upper() == "Y":
    # get computer input
    computer = getComputerInput()
    
    # get player 1 input
    inputOk = False
    while inputOk == False:
        player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()
        if (player1 in choices.values()):
            inputOk = True
        else:
            print("Error: invalid selection. Try again.")

    # compare input and output winner
    if (player1 == computer):
        print("Tie, both players chose {}").format(player1)
    elif (player1 == "rock" and computer == "paper"):
        print("The computer wins, paper covers rock.")
    elif (player1 == "rock" and computer == "scissors"):
        print("Player 1 wins, rock smashes scissors.")
    elif (player1 == "rock" and computer == "lizard"):
        print("Player 1 wins, rock smashes lizard")
    elif (player1 == "rock" and computer == "spock"):
        print("The computer wins, Spock vaporizes rock.")
    elif (player1 == "paper" and computer == "rock"):
        print("Player 1 wins, paper covers rock.")
    elif (player1 == "paper" and computer == "scissors"):
        print("The computer wins, scissors cut paper.")
    elif (player1 == "paper" and computer == "lizard"):
        print("The computer wins, lizard eats paper.")
    elif (player1 == "paper" and computer == "spock"):
        print("Player 1 wins, paper disproves Spock")
    elif (player1 == "scissors" and computer == "rock"):
        print("The computer wins, rock smashes scissors.")
    elif (player1 == "scissors" and computer == "paper"):
        print("Player 1 wins, scissors cut paper.")
    elif (player1 == "scissors" and computer == "lizard"):
        print("Player 1 wins, scissors decapitate lizard.")
    elif (player1 == "scissors" and computer == "spock"):
        print("The computer wins, Spock smashes scissors.")
    elif (player1 == "lizard" and computer == "rock"):
        print("The computer wins, rock smashes lizard.")
    elif (player1 == "lizard" and computer == "paper"):
        print("Player 1 wins, lizard eats paper.")
    elif (player1 == "lizard" and computer == "scissors"):
        print("The computer wins, scissors decapitate lizard.")
    elif (player1 == "lizard" and computer == "spock"):
        print("Player 1 wins, lizard poisons Spock.")
    elif (player1 == "spock" and computer == "rock"):
        print("Player 1 wins, Spock vaporizes rock.")
    elif (player1 == "spock" and computer == "paper"):
        print("The computer wins, paper disproves Spock.")
    elif (player1 == "spock" and computer == "scissors"):
        print("Player 1 wins, Spock smashes scissors.")
    elif (player1 == "spock" and computer == "lizard"):
        print("The computer wins, lizard poisons Spock.")

    # prompt for continuation or termination
    playAgain = raw_input("Enter 'Y' to play again: ")