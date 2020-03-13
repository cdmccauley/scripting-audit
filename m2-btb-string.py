# demonstrates: imports
import os, time

# demonstrates: function definition, function return
def getString():
    print""
    #get string from user
    a_string=raw_input("Please enter a string: ")
    return a_string

# demonstrates: function call, exception handling
def printMenu():
    time.sleep(2) # display last entry
    os.system('cls') # clear ui
    print ""
	#print menu of options
    print " Menu:"
    print "1: Print the string in reverse..."
    print "2: Print the length of the string..."
    print "3: Print the string in uppercase..."
    print "4: Print the string in lowercase..."
    print "5: Enter new string..."
    print "6: Exit..."
    print ""
	#get menu choice
    inputOK=0
    while inputOK==0:
        targetString=raw_input("Enter an item number from the menu:")
        try:
            target=int(targetString)
        except ValueError:
            target=0 #set value as an error
        if (target>0) and (target <7):
                inputOK=1
        else:
            print "     Error: a single digit in range, please..."
    print ""
    return target

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
    choice = printMenu()
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



