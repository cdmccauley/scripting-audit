# We will start this guided practice with a demonstration of list declaration.
# An empty list can be simply declared by assigning an opening and closing bracket to a variable.
demoList = []

# A list can also be initialized when it is declared by providing a comma separated list of values.
demoList = ["rock", "paper", "scissors"]

# Whether a list is declared empty or with provided values it can have an item added to the end of it at any time by passing a value to the append method of the list.
demoList.append("Spock")

# To access the values stored in the list the square bracket syntax can be used with a number that represents the postion of the item in the list.
# This number is referred to as the index of the item and is assigned automatically based on the order that the items were assigned to the list.
# Because we are working with computers the first item in the list is always assigned an index of 0.
demoVariable = demoList[0]
print demoVariable # prints the word "rock"
demoVariable = demoList[1]
print demoVariable # prints the word "paper"

# The number used in the square bracket syntax can be stored in a variable as well.
indexVariable = 2
demoVariable = demoList[indexVariable]
print demoVariable # prints the word "scissors"

# Once a list index has been assigned a value the square bracket syntax can also be used to change the value at that index.
print demoList[3] # prints the word "Spock"
demoList[3] = "lizard" # overwrites "Spock" with "lizard"
print demoList[3] # prints the word "lizard"

# Lists can also be paired with the "in" keyword which has two uses, the first is to check if a value is present in the list.
if ("Spock" in demoList): # evaluates to False because "Spock" was overwritten by "lizard"
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

demoList.append("Spock")

if ("Spock" in demoList): # evaluates to True because "Spock" was appended to the end of the list.
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

# The second use for the "in" keyword is to create a loop that iterates once for each item in a list.
# This type of loop is referred to as a for or for-each loop.
# The syntax used to define a for-each loop declares a variable which each item in the list will be stored in before the for-each codeblock is run.
for demoItem in demoList:
    print demoItem # prints the first value in demoList then prints the next value and continues until all values have been printed.

# The for loop can also be used with the range function to iterate a set number of times.
# The range function returns a list of numbers starting from the first argument to the second argument.
for i in range(0, len(demoList)): # for-each number from 0 to the last index of the demoList.
    print "{}. ".format(i) + demoList[i] # prints the index and first value in demoList then prints the next index and value and continues until all indexes and values have been printed.

# The for loop is only one type of loop available in Python.
# The other type of loop, a while loop, will run until the evaluation of a condition returns a False value.
# The syntax used to define a while loop declares the condition that will be evaluated to determine when the loop will finish.
playAgain = "Y"
while (playAgain.upper() == "Y"):
    playAgain = raw_input("Enter 'Y' to play again: ")

# These 3 lines of code will continuously prompt the user for input as long as they enter a "Y" or "y".
# If anything else is entered, the loop condition will be evaluated to False and the loop will exit.
# In addition to an example of a loop, this can also be an example of input validation.
# If the players enter a valid value, the loop will continue to run.
# If the players enter an invalid value, the loop will exit.

# This concept could be reversed and a loop could be written to run while the user is entering invalid values.
choices = ["rock", "paper", "scissors", "lizard", "spock"]
inputOk = False
while (inputOk == False):
    player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or Spock: ").strip().lower()
    if (player1 in choices):
        inputOk = True

# In these lines of code the user will be prompted to enter a value until the value entered is also in the list named choices.
# This type of validation can be used to ensure that a value entered by the user will not cause the rest of the script to behave in an unexpected way or crash.

# These two loops could also be paired together by nesting one inside the other. 
# This would cause the script to prompt the user for valid input until they enter valid input and decide to stop.
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

# After nesting the loops, there is almost enough code for a complete game of rock, paper, scissors, lizard, Spock that uses validation and is replayable.

# To complete the practice portion of this lesson you will add some user feedback and another loop to the demonstration code and test that it works.
# Implement code for the following items then take a screenshot that shows the script running with an invalid value and valid value from each player along with the game being played again and then exited.

# 1. Add branching to display a message that will inform player 1 they have entered an invalid value.
# 2. Add an additional while loop that will prompt player 2 for input until it is a valid choice, include branching to display a message that will inform player 2 they have entered an invalid value.