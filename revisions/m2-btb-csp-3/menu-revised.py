# imports
import os, time

# get string from user
def getString():
    userString = raw_input("Please enter a string: ")
    return userString

# print a menu of options
def printMenu():
    time.sleep(2) # display last entry
    os.system('cls') # clear ui
    print "Menu:"
    print "1: Print the string in reverse..."
    print "2: Print the length of the string..."
    print "3: Print the string in uppercase..."
    print "4: Print the string in lowercase..."
    print "5: Enter new string..."
    print "6: Exit..."
    print ""

# get menu item from user
#NOTE: working here
def getMenuItem():
    menuItem = 0
    userInput = raw_input("Enter an item number from the menu:")
    try:
        menuItem = int(userInput)
    except:
        print "Error: Input must be a number 1-6."
    if menuItem > 0 and menuItem < 7:
        return menuItem
    else:
        getMenuItem()

# demonstrates: function parameter
def revString(user_string):
    rev_string=''
    x=len(user_string) #gets the length of a string
    for i in range(0, x):
        rev_string=user_string[i]+rev_string
    print "Your string in reverse:",rev_string
    if (user_string.lower())== (rev_string.lower()):
        print "Your string is a palindrome!"
    print ""

# demonstrates: function arguments
user_string = getString()
again=True
while (again):
    printMenu()
    choice = getMenuItem()
	#create output
    if choice==1:
        revString(user_string)
    elif choice==2: 
        print "The length of your string is: ",str(len(user_string))
    elif choice==3: 
        print "Your string in all-Caps: ",user_string.upper()
    elif choice==4: 
        print "Your string in lowercase: ",user_string.lower() 
    elif choice==5:
        user_string = getString()
    else:  #choice==6: 
        again=False
        print ""
print ""
pause=raw_input("Press Enter to close the window...")



