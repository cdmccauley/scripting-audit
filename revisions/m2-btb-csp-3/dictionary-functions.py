# We'll start this practice with a demonstration of dictionary and function declaration.
# An empty dictionary can be simply declared by assigning an opening and closing curly brace to a variable.
demoDictionary = {}

# A dictionary can also be initialized when it is declared by providing a comma separated list of key-value pairs separated by a colon.
demoDictionary = { "key": "value", "word": "definition", "course": 1036 }

# Whether the dictionary is declared empty or with provided values it can have items added to it at any time if the key being added does not already exist.
# Two ways to add items to a dictionary are by assigning a value using square bracket syntax or the update function.
# When using square brackets to add an item to the dictionary the key is specified in the square brackets and the value is assigned to that key in the dictionary.
demoDictionary[1] = "one"

# When using the update function the key(s) and value(s) are specified as a dictionary literal with curly braces, colons, and commas; much like the syntax used when initializing.
demoDictionary.update({ "[": "left-bracket", "]": "right-bracket" })

# To access the values stored in the dictionary the square bracket syntax or get function can be used with a key for the value.
print demoDictionary["key"] # prints the word "value"
demoVariable = demoDictionary.get(1)
print demoVariable # prints the word "one"

# Notice that this single dictionary can have keys of different data types and values of different data types.
# This can be convenient but can also cause issues if trying to access values with a key of the wrong data type.
print demoDictionary.get("1") # prints "None" because the specified key does not exist as a string.

# The get function is a function that requires an argument and returns a value.