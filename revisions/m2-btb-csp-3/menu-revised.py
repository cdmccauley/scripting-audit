users = { 1234: 'Robbie Sweeten', 5678: 'Stephen Christensen' }

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
    for value in users.values():
        if name in value:
            response = 'User found'
        else:
            response = 'User not found'
    return response

print addOrUpdateUser(2468, 'Carey Anson')
printUserIDs()
print addOrUpdateUser(5678, 'The Steve')
printUserNames()
print removeUser(1234)

printUsers()