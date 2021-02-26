# reversing a string, demonstrating functions


# get user input

# reverse string

# continue?

def getInputString():
    userInput = raw_input("enter string")
    return userInput

def printMenu():
    print "Menu:"
    print "1. Enter new string"
    print "2. Check if string is palindrome"
    print "3. Quit"

def menuPrompt():
    menuItem = raw_input("Please enter menu item (1-3): ")
    return menuItem

def reverseString(userString):
    return ""

def exitScript():
    return False

def menuSelection(item):
    if item == "1":
        getInputString()
    elif item == "2":
        reverseString(item)
    elif item == "3":
        exitScript()

