#
# installs BeautifulSoup on each run
#
import subprocess
import sys
from bs4 import BeautifulSoup

if("bs4" not in sys.modules.keys()):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "BeautifulSoup"])

# print("numpy" in sys.modules)

# #
# # script for web crawler
# #

# # imports
# import urllib
# from bs4 import BeautifulSoup

# # declarations
# url = "https://www.brummett.info/"

# # functions
# def getPage(url):
#     try:
#         page = urllib.urlopen(url)
#         soup = BeautifulSoup(page, "html.parser")
#     except:
#         print("error: " + url + " not found.")

# getPage(url)