# variable declarations
users = { 1234: 'AJ Hepler', 5678: 'Robbie Sweeten', 1357: 'Stephen Christensen' }
output = ''

# function declarations
def addOrUpdateUser(id, name):
    if id not in users.keys(): # check if user id does not exist
        response = 'User ' + name + ' added' # user id does not exist, add user
    else:
        response = 'User ' + users[id] + ' updated to ' + name # user id exists, update user
    users[id] = name
    return response

def removeUser(id):
    if id in users.keys(): # check if user id exists
        response = 'User ' + users[id] + ' removed'
        users.pop(id) # user id exists, remove user using id
    else:
        response = 'User ID' + id + ' not found'
    return response

def printUsers():
    for key in users.keys(): # loop through keys and store user id in key
        print str(key) + ': ' + users[key] # print user key and user name by accessing key

def searchUserNames(name):
    response = 'User ' + name + ' not found'
    for value in users.values(): # loop through values and store user name in value
        if name in value: # if the name provided matches the user name in value
            response = 'User ' + name + ' found' 
    return response

# begin script
# call functions with arguments and store returned values
output = addOrUpdateUser(2468, 'Carey Anson')
print output
output = searchUserNames('Carey Anson')
print output

# call functions with arguments and use returned values
print addOrUpdateUser(1357, 'The Steve')
print searchUserNames('Stephen Christensen')

print removeUser(1234)
print searchUserNames('AJ Hepler')

# call function that does not require arguments or return a value
printUsers()