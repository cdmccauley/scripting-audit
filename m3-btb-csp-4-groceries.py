# imports
import os

# declarations
groceryList = ['spam', 'eggs']

# demonstrates open
# open file or create
listFile = open('GroceryList.txt', 'w')

# iterate over list writing and printing
for item in groceryList:
    # demonstrates write
    listFile.write(item + '\n')
    print(item)

# demonstrates close
# close file
listFile.close()