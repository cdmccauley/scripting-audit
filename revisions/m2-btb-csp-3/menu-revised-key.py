# variable definitions, accessbile through entire script
userList = ['chapmang', 'cleesej', 'idlee']
userToRemove = ''
outcome = ''

# function definitions
def printList(): # function without parameter
    print 'Usernames:'
    for user in userList:
        print user

def removeUser(user): # function with parameter, user
    if user in userList:
        userList.remove(user)
        feedback = "User removed" # this variable is only accessible inside the removeUser function
    else:
        feedback = "User not found"
    return feedback # return value where function was called

# script
printList() # call custom function, does not need argument

userToRemove = raw_input('Enter username to remove from the user list: ')
outcome = removeUser(userToRemove) # call custom function with argument and store value returned from function
print outcome
printList()