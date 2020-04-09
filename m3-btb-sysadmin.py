# imports
import os
import shutil

# declarations
fileName = "deadEmployees.txt"
pathName = os.getcwd() + "\\Users2\\"
data = False

# open file and read data
try:
    userFile = open(fileName, "r")
    userList = userFile.readlines()
    userFile.close()
    data = True
except:
    print("Error: Problem reading from file.")

# no errors, clean data and remove dir
if (data):
    i = 0
    userList.remove(userList[0]) # remove header
    for user in userList:
        userList[i] = user.strip()[:-15] # clean whitespace and domain
        i = i + 1
    for user in userList:
        userPath = pathName + user # create path name
        print(userPath)
        shutil.rmtree(userPath) # remove dir