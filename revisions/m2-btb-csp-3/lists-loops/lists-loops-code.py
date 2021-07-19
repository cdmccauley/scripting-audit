demoList = []

demoList = ["rock", "paper", "scissors"]

demoList.append("Spock")

demoVariable = demoList[0]
print demoVariable # prints the word "rock"
demoVariable = demoList[1]
print demoVariable # prints the word "paper"

indexVariable = 2
demoVariable = demoList[indexVariable]
print demoVariable # prints the word "scissors"

print demoList[3] # prints the word "Spock"
demoList[3] = "lizard" # overwrites "Spock" with "lizard"
print demoList[3] # prints the word "lizard"

if ("Spock" in demoList): # evaluates to False because "Spock" was overwritten by "lizard"
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

demoList.append("Spock")

if ("Spock" in demoList): # evaluates to True because "Spock" was appended to the end of the list.
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

for demoItem in demoList:
    print demoItem # prints the first value in demoList then prints the next value and continues until all values have been printed.

for i in range(0, len(demoList)): # for-each number from 0 to the last index of the demoList.
    print "{}. ".format(i) + demoList[i] # prints the index and first value in demoList then prints the next index and value and continues until all indexes and values have been printed.

playAgain = "Y"
while (playAgain.upper() == "Y"):
    playAgain = raw_input("Enter 'Y' to play again: ")

choices = ["rock", "paper", "scissors", "lizard", "spock"]
inputOk = False
while (inputOk == False):
    player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or Spock: ").strip().lower()
    if (player1 in choices):
        inputOk = True

playAgain = "Y"
choices = ["rock", "paper", "scissors", "lizard", "spock"]
while (playAgain.upper() == "Y"):
    inputOk = False
    while (inputOk == False):
        player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or Spock: ").strip().lower()
        if (player1 in choices):
            inputOk = True
    # get player2 input
    # decide winner
    playAgain = raw_input("Enter 'Y' to play again: ")