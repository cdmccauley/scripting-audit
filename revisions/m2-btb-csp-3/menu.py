again = True
while (again):
    print ""
    print""
	#get string from user
    user_string=raw_input("Please enter a string: ")
    print""
	#print menu of options
    print " Menu:"
    print "1: Print the string in reverse..."
    print "2: Print the length of the string..."
    print "3: Print the string in uppercase..."
    print "4: Print the string in lowercase..."
    print "5: Quit..."
    print ""
	#get menu choice
    inputOK=0
    while inputOK==0:
            targetString=raw_input("Enter an item number from the menu:")
            try:
                target=int(targetString)
            except ValueError:
                target=0 #set value as an error
            if (target>0) and (target <6):
                    inputOK=1
            else:
                print "     Error: a single digit in range, please..."
    print ""
	#create output
    if target==1:
            rev_string=''
            x=len(user_string) #gets the length of a string
            for i in range(0, x):
                rev_string=user_string[i]+rev_string
            print "Your string in reverse:",rev_string
            if (user_string.lower())== (rev_string.lower()):
                print "Your string is a palindrome!"
    elif target==2: 
            print "The length of your string is: ",str(len(user_string))
    elif target==3: 
            print "Your sting in all-Caps: ",user_string.upper()
    elif target==4: 
            print "Your sting in lowercase: ",user_string.lower() 
    else:  #target==5: 
            again=False
            print ""
            print ""
pause=raw_input("Press Enter to close the window...")



