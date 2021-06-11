# We'll start this practice with a demonstration of dictionary and function declaration.
# An empty dictionary can be simply declared by assigning an opening and closing curly brace to a variable.
demoDictionary = {}
# A dictionary can also be initialized when it is declared by providing a comma separated list of key-value pairs separated by a colon.
demoDictionary = { "key": "value", "word": "definition" }
# Whether the dictionary is declared empty or with provided values it can have items added to it at any time if the key being added does not already exist.
# Two ways to add items to a dictionary are using square brackets or the update function.
# When using square brackets to add an item to the dictionary the key is specified in the square brackets and the value is assigned to that key in the dictionary.
demoDictionary[1] = "one"
# When using the update function the key(s) and value(s) are specified as a dictionary literal with curly braces, colons, and commas; much like the syntax used when initializing.
demoDictionary.update({ "[": "left-bracket", "]": "right-bracket" })