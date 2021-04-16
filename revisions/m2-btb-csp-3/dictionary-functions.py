# variable declarations
numbers = { 1: 'one', 2: 'two', 3: 'tree' }
output = ''

# function declarations
def addPairOrUpdateValue(dictionary, key, value):
    if dictionary.has_key(key): # check if key exists
        response = 'Value %s updated to %s.' %(dictionary[key], value) # key exists, update value
    else:
        response = 'Pair "%s: %s" added.' %(key, value) # key does not exist, add key/value
    dictionary[key] = value
    return response

def removePairByKey(dictionary, key):
    if dictionary.has_key(key): # check if key exists
        response = 'Pair "%s: %s" removed.' %(key, dictionary[key])
        dictionary.pop(key) # key exists, remove key/value
    else:
        response = 'Key %s not found.' %(key)
    return response

def removePairByValue(dictionary, value):
    response = 'Value %s not found.' %(value)
    for key in dictionary.copy().keys(): # iterate over copy so no error is caused when removing from original
        if dictionary[key] == value:
            dictionary.pop(key) # value was found, remove key/value
            response = 'All instances of %s removed.' %(value)
    return response

def keyOrValue(dictionary, item):
    if item in dictionary.keys() and item in dictionary.values():
        response = '%s is a key and a value.' %(item)
    elif item in dictionary.keys():
        response = '%s is a key.' %(item)
    elif item in dictionary.values():
        response = '%s is a value.' %(item)
    else:
        response = '%s is not a key or a value.' %(item)
    return response

def printPairs(dictionary):
    for key in dictionary.keys():
        print '%s: %s' %(key, dictionary[key])

# begin script
# call functions with arguments and store returned values

# call functions with arguments and use returned values

# call function that does not require arguments or return a value

print addPairOrUpdateValue(numbers, 3, 'three')
printPairs(numbers)

print addPairOrUpdateValue(numbers, 4, 'four')
printPairs(numbers)

print removePairByKey(numbers, 1)
printPairs(numbers)

print removePairByValue(numbers, 'two')
printPairs(numbers)