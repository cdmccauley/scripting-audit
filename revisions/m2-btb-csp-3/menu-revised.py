users = { 1234: 'Robbie Sweeten', 5678: 'Stephen Christensen' }
output = ''

def addOrUpdateUser(id, name):
    if id not in users.keys():
        response = 'User added'
    else:
        response = 'User updated'
    users[id] = name
    return response

def removeUser(id):
    if id in users.keys():
        users.pop(id)
        response = 'User removed'
    else:
        response = 'User not found'
    return response

def printUsers():
    for key in users.keys():
        print str(key) + ': ' + users[key]

def searchUserNames(name):
    response = 'User not found'
    for value in users.values():
        if name in value:
            response = 'User found'
    return response

output = addOrUpdateUser(2468, 'Carey Anson')
print output
output = searchUserNames('Carey Anson')
print output

output = addOrUpdateUser(5678, 'The Steve')
print output
output = searchUserNames('Stephen Christensen')
print output

output = removeUser(1234)
print output
output = searchUserNames('Robbie Sweeten')
print output

printUsers()