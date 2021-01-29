again = True
while(again):
	#get string from user
    userString = raw_input("Please enter a string: ")

	#print menu of options
    print("Menu:")
    print("1: Print the string in reverse...")
    print("2: Print the length of the string...")
    print("3: Print the string in uppercase...")
    print("4: Print the string in lowercase...")
    print("5: Quit...")

	#get menu choice
    inputOK = False
    while(inputOK == False):
        menuItem = raw_input("Enter an item number from the menu: ")

        try:
            menuItem = int(menuItem)
        except ValueError:
            menuItem = 0

        if(menuItem > 0) and (menuItem < 6):
            inputOK=1
        else:
            print "Error: Invalid Entry"

	#create output
    if(menuItem == 1):
        revString = ""
        stringLength = len(userString)

        for index in range(stringLength, 0, -1):
            revString = revString + userString[index]

        print("Your string in reverse:", revString)

        if(userString.lower() == revString.lower()):
            print("Your string is a palindrome!")
        
    elif target==2: 
            print "The length of your string is: ",str(len(userString))
    elif target==3: 
            print "Your sting in all-Caps: ",userString.upper()
    elif target==4: 
            print "Your sting in lowercase: ",userString.lower() 
    else:  #target==5: 
            again=False
            print ""
            print ""
pause=raw_input("Press Enter to close the window...")