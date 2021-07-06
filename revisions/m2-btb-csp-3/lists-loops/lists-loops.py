# We will start this guided practice by tackling the objective of using a loop to repeat a script without exiting.
# Hour 7 of the texbook introduces two types of loops that use different methods to repeat a block of code.
# The first loop, a for loop, will run a set number of times.
# If we use this loop we could either hard-code a number of times for players to play or ask them to decide how many times to play.
# The second loop, a while loop, will run until the evaluation of a condition returns a False value.
# If we use this loop for our game the players could play until the they want to quit.

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
# This concept could be reversed, a loop could be written to run while the players are entering invalid values.