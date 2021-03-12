# variable definitions
groceryList = ['Spam', 'Eggs']
itemToRemove = ''
outcome = ''

# function definitions
def printList(): # function without parameter
    for item in groceryList:
        print item

def removeItem(item): # function with parameter
    if item in groceryList:
        groceryList.remove(item)
        feedback = "Item removed"
    else:
        feedback = "Item not found"
    return feedback # return value where function was called

# script
printList() # call custom function

itemToRemove = raw_input('Enter an item to remove from the grocery list: ')
outcome = removeItem(itemToRemove) # store value returned from function
print outcome
printList()

# end script
print 'Goodbye'