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
    if (isinstance(value, dict)):
        demoDictionary.update(value)
    else:
        print "invalid argument"

updateWrapper(["list"]) # prints "invalid argument" because a list is not a dictionary

updateWrapper({"parameter": "argument"}) # updates demoDictionary with a new key-value pair.
print demoDictionary.get("parameter") # prints "argument"

# Notice that the demoDictionary is being used inside of the function even though it has been declared outside of the function and it wasn't passed in as an argument.
# This works because the variable demoDictionary was declared in the main body of the code and is therefore in the global scope.
# There is another type of scope, which is called local scope, and each function has it's own local scope.
# Items declared in the global scope, including variables and functions, can be accessed in a local scope.
# However, items declared in a local scope can not be accessed in the global scope or other local scopes.
# It may seem that this behavior would be problematic because it would require all items to be declared in the global scope if they are to be used in any scope.
# That is not the case though because functions may use the return keyword to send a value back to the scope from which they were called.
# The inclusion of the return keyword alongside parameters and scope are what help functions make code easier to maintain and reuse.

# To demonstrate portability with parameters and return we can create a function that will indicate whether a dictionary has a specific value, much like the function has_key that dictionaries already have.
# For the scope demonstration we will create a variable with the same name as a variable we intend to use in the function to show that each is in its own scope.
inValues = "this variable was declared in global scope"

# Since our function will not be defined on dictionaries it will need to accept a dictionary and a value as an argument and it will return a boolean indicating if the value is in the dictionary.
# This function could be copied to another Python script and could be used for dictionaries in that script.
def has_value(dictionary, value):
    inValues = False
    if (value in dictionary.values()):
        inValues = True
    return inValues

# Before we call the has_value function we will display the value of the global variable inValues.
print inValues # prints "this variable was declared in global scope"

# Now we can use our has_value function by calling it with the demoDictionary and a value that should still be inside the dictionary.
# The has_value function returns a boolean to the global scope that can be stored in variable and used in the if statement.
result = has_value(demoDictionary, 1036)
if (result):
    print "value found"
else:
    print "value not found"

# When the has_value function was called, a variable named inValues was created within its local scope and assigned a boolean value.
# To show that this operation had no effect on the global variable of the same name we can print the global variable.
print inValues # prints "this variable was declared in global scope"

# One last consideration that hasn't been addressed is how this is all put together.
# With more constructs being introduced, comments and organization become more and more important.
# Every simple script can be organized into sections: imports, global variable declarations, function declarations, and the code that "drives" the script.
# The reason to organize scripts in this order is due to dependency.
# Imported modules will satisfy their own dependencies but you may need those modules to initialize your variables, use in your functions, or use in your driver code so they should be declared first.
# Global variables may use imported modules to be initialized and may need to be available for your functions and driver code so they should be declared second.
# Functions may use imported modules or global variables and be used in your driver code so they should be declared third.
# Since functions may also be dependent on other functions, the calling functions should be declared after the functions they call.
# Finally, driver code ties everything together and will need access to everything else so it should always be declared last.

# practice...add your own key-value pair to the dictionary using the update function or square bracket syntax then use the has_key function to check if your key exists in the dictionary and print a message indicating it was found or not found