import os
import inspect

sigData = 'Infected'
logFile = open('detected-log.txt', 'w+')

def search(path):
    fileList = os.listdir(path)
    for fileName in fileList:
        if os.path.isdir(path + os.path.sep + fileName):
            search(path + os.path.sep + fileName)
        elif fileName[-3:] == '.py':
            for line in open(path + os.path.sep + fileName):
                if sigData in line:
                    print(path + os.path.sep + fileName)
                    logFile.write(path + os.path.sep + fileName + '\n')

search(os.getcwd())

logFile.close()