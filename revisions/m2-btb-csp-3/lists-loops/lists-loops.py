# We will start this guided practice with a demonstration of list and loop declaration.
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

# Once an index has been assigned a value the square bracket syntax can also be used to change the value at that index.
print demoList[3] # prints the word "Spock"
demoList[3] = "lizard" # overwrites "Spock" with "lizard"
print demoList[3] # prints the word "lizard"

# Lists can also be used with the "in" keyword which has two uses, the first is to check if a value is present in the list.
if ("Spock" in demoList): # evaluates to False
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

demoList.append("Spock")

if ("Spock" in demoList): # evaluates to True
    print "The Search for Spock is over."
else:
    print "Continue The Search for Spock."

# The second use for the "in" keyword is to create a loop that iterates once for each item in a list.
# This type of loop is referred to as a foreach loop.
# The syntax of a foreach loop declares a variable which each item in the list will be stored in before the foreach codeblock is run.
for demoItem in demoList:
    print demoItem # prints each value stored in demoList

# 



# We will start this guided practice by tackling the objective of using a loop to repeat a script without exiting.
# Hour 7 of the texbook introduces two types of loops that use different methods to repeat a block of code.
# The first loop, a for loop, will run a set number of times.
# If we use this loop we could either hard-code a number of games for players to play or ask them to decide how many games to play.
# The second loop, a while loop, will run until the evaluation of a condition returns a False value.
# If we use this loop for our game the players could play until they want to quit.

# For our game it seems more appropriate to allow the players to play until they decide to quit and therefore will use a while loop.
# We can assume the players want to play the game when they first invoke the script and can use this assumption to create a condition to start the game.
# When the game is over we can prompt the players for input indicating whether they would like to run the loop again or exit the script.
playAgain = "Y"
while playAgain.upper() == "Y":
    # get player choices
    # decide outcome
    playAgain = raw_input("Enter 'Y' to play again: ")

# When running these 3 lines of code you will be continuously prompted for input as long as you enter a "Y" or "y".
# If anything else is entered, the loop condition will be evaluated to False and the script will exit.
# In addition to an example of a loop, this can also be an example of input validation.
# If the players enter a valid value, the loop will continue to run.
# If the players enter an invalid value, the loop will exit.
# This concept could also be reversed, a loop could be written to run while the players are entering invalid values.
playAgain = "Y"
while playAgain.upper() == "Y":
    inputOK = False
    while inputOK == False:
        player1 = raw_input("Player 1, choose: rock, paper, scissors, lizard, or spock: ").strip().lower()
    # decide outcome
    playAgain = raw_input("Enter 'Y' to play again: ")