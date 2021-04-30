# variable declarations
numbers = { 1: 'one', 2: 'two', 3: 'tree' }
output = ''

# function declarations
def addPairOrUpdateValue(dictionary, key, value):
    if dictionary.has_key(key): # check if key exists
        response = 'Value {} updated to {}.'.format(dictionary[key], value) # key exists, function will update value
    else:
        response = 'Pair "{}: {}" added.'.format(key, value) # key does not exist, function will add key/value
    dictionary[key] = value # update or add
    return response

def removePairByKey(dictionary, key):
    if dictionary.has_key(key): # check if key exists
        response = 'Pair "{}: {}" removed.'.format(key, dictionary[key])
        dictionary.pop(key) # key exists, remove key/value
    else:
        response = 'Key {} not found.'.format(key)
    return response

def removePairByValue(dictionary, value):
    response = 'Value {} not found.'.format(value)
    for key in dictionary.copy().keys(): # iterate over copy so no error is caused when removing from original
        if dictionary[key] == value:
            dictionary.pop(key) # value was found, remove key/value
            response = 'All instances of {} removed.'.format(value)
    return response

def keyOrValue(dictionary, item):
    if item in dictionary.keys() and item in dictionary.values():
        response = '{} is a key and a value.'.format(item)
    elif item in dictionary.keys():
        response = '{} is a key.'.format(item)
    elif item in dictionary.values():
        response = '{} is a value.'.format(item)
    else:
        response = '{} is not a key or a value.'.format(item)
    return response

def printPairs(dictionary):
    for key in dictionary.keys():
        print '{}: {}'.format(key, dictionary[key])

# begin script

# call function with arguments and store return
output = addPairOrUpdateValue(numbers, 3, 'three')
print output
printPairs(numbers)

# call functions with arguments and use return
print addPairOrUpdateValue(numbers, 4, 'four')
printPairs(numbers)

print removePairByKey(numbers, 1)
printPairs(numbers)

print removePairByValue(numbers, 'two')
printPairs(numbers)