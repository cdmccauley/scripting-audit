# We'll start this practice with a demonstration of dictionary and function declaration.
# An empty dictionary can be simply declared by assigning an opening and closing curly brace to a variable.
demoDictionary = {}

# A dictionary can also be initialized when it is declared by providing a comma separated list of key-value pairs separated by a colon.
demoDictionary = { "key": "value", "word": "definition", "course": 1036 }

# Whether the dictionary is declared empty or with provided values it can have items added to it at any time if the key being added does not already exist.
# If the key already exists the value that is paired with that key will simply be overwritten.
# Two ways to add or update items in a dictionary are by assigning a value using square bracket syntax or by using the update function.
# When using square brackets to add an item to the dictionary the key is specified in the square brackets and the value is assigned to that key in the dictionary.
demoDictionary[1] = "one"

# When using the update function the key(s) and value(s) are specified as a dictionary literal with curly braces, colons, and commas; much like the syntax used when initializing.
demoDictionary.update({ "[": "left-bracket", "]": "right-bracket" })

# To access the values stored in the dictionary the square bracket syntax or get function can be used with a key for the value.
demoVariable = demoDictionary["key"]
print demoVariable # prints the word "value"
demoVariable = demoDictionary.get(1)
print demoVariable # prints the word "one"

# Notice that this single dictionary can have keys of different data types and values of different data types.
# This can be convenient but can also cause issues if trying to access values with a key of the wrong data type.
print demoDictionary.get("1") # prints "None" because the specified key does not exist as a string.

# We've used two of the dictionary's functions so far, get and update.
# The update function is a function that requires an argument but does not return a value.
# The get function is a function that requires an argument and returns a value.
# To better understand what this means we can create some functions to demonstrate these concepts.
# We'll start with the function definition which uses the "def" keyword and is followed by the function name with parentheses and a colon.
# Any code within the function's code block, which is defined by the indentation, will be run when the function is called.
def demoFunction():
    print "This message comes from the demoFunction code block"

# The demoFunction is an example of a function that takes no arguments and returns no values.
# Since the demoFunction does not require any arguments it can be called with nothing in the parentheses.
demoFunction() # prints "This message comes from the demoFunction code block"

# To create a function that requires arguments we can include one or more parameters inside the parentheses when defining the function.
# You can think of a parameter as a variable that will hold the value of an argument included in the function call.
# To demonstrate a function with a parameter we can create a "wrapper" function for the update function.
# The update "wrapper" will accept an argument, check if it is a dictionary, and either update the demoDictionary or print an error.
def updateWrapper(value):
    if (type(value) == type(demoDictionary)):
        demoDictionary.update(value)
    else:
        print "invalid argument"

updateWrapper(["list"]) # prints "invalid argument" because a list is not a dictionary

updateWrapper({"parameter": "argument"}) # updates demoDictionary with a new key-value pair.
print demoDictionary.get("parameter") # prints "argument"

# Notice that the demoDictionary is being used inside of the function even though it has been declared outside of the function.
# This works because the variable demoDictionary was declared in the main body of the code and is therefore in the global scope.
# There is another type of scope which is called local scope, and each function has it's own local scope.
# Although variables declared in the global scope can be accessed in a local scope, variables declared in a local scope can not be accessed in the global scope.
# Local scope is one of the features of functions and is what helps them make code easier to maintain and reuse.
