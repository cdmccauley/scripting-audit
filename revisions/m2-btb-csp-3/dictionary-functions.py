# variable declarations
users = { 1234: 'AJ Hepler', 5678: 'Robbie Sweeten', 1357: 'Stephen Christensen' }
output = ''

# function declarations
def addOrUpdatePair(dictionary, key, value):
    if dictionary.has_key(key): # check if key exists
        response = 'Value ' + dictionary[key] + ' updated to ' + value # key exists, update value
    else:
        response = 'Value ' + value + ' added' # key does not exist, add key/value
    dictionary[key] = value
    return response

def removePairById(dictionary, key):
    if dictionary.has_key(key): # check if user key exists
        response = 'User ' + dictionary[key] + ' removed'
        dictionary.pop(key) # user key exists, remove user using key
    else:
        response = 'User ID' + key + ' not found'
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
output = addOrUpdatePair(users, 2468, 'Carey Anson')
print output
output = searchUserNames('Carey Anson')
print output

# call functions with arguments and use returned values
print addOrUpdatePair(users, 1357, 'The Steve')
print searchUserNames('Stephen Christensen')

print removePairById(users, 1234)
print searchUserNames('AJ Hepler')

# call function that does not require arguments or return a value
printUsers()