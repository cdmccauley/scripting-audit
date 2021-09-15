# global declarations
numbers = { 1: 'one', 2: 'two', 3: 'three' }

# functions
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

# script
print keyOrValue(numbers, 'four')
print keyOrValue(numbers, 2)