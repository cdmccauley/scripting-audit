# variable definitions
groceryList = ['Spam', 'Eggs']

# function definitions
def addItem(item):
    groceryList.append(item)

def removeItem(item):
    if item in groceryList:
        groceryList.remove(item)
        feedback = "Item removed"
    else:
        feedback = "Item not found"
    return feedback

def printList():
    for item in groceryList:
        print item

# script
printList()

itemToAdd = raw_input('Enter an item to add to the grocery list: ')
addItem(itemToAdd)
printList()

itemToRemove = raw_input('Enter an item to remove from the grocery list: ')
outcome = removeItem(itemToRemove)
print outcome
printList()

print 'Goodbye'