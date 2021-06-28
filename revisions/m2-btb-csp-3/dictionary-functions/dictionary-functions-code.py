demoDictionary = {}

demoDictionary = { "key": "value", "word": "definition", "course": 1036 }

demoDictionary[1] = "one"

demoDictionary.update({ "[": "left-bracket", "]": "right-bracket" })

demoVariable = demoDictionary["key"]
print demoVariable # prints the word "value"
demoVariable = demoDictionary.get(1)
print demoVariable # prints the word "one"

print demoDictionary.get("1") # prints "None" because the specified key does not exist as a string.

def demoFunction():
    print "This message comes from the demoFunction code block"

demoFunction() # prints "This message comes from the demoFunction code block"

def updateWrapper(value):
    if (isinstance(value, dict)):
        demoDictionary.update(value)
    else:
        print "invalid argument"

updateWrapper(["list"]) # prints "invalid argument" because a list is not a dictionary

updateWrapper({"parameter": "argument"}) # updates demoDictionary with a new key-value pair.
print demoDictionary.get("parameter") # prints "argument"

inValues = "this variable was declared in global scope"

def has_value(dictionary, value):
    inValues = False
    if (value in dictionary.values()):
        inValues = True
    return inValues

print inValues # prints "this variable was declared in global scope"

result = has_value(demoDictionary, 1036)
if (result):
    print "value found"
else:
    print "value not found"

print inValues # prints "this variable was declared in global scope"