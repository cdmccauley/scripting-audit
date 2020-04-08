#
# install BeautifulSoup if not installed
#
import subprocess
import sys

try:
    from bs4 import BeautifulSoup
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

#
# web crawler
#

# imports
import urllib
import logging

# declarations
url = "https://www.brummett.info/"

# functions
def getPage(url):
    hrefs = []
    try:
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if (href[:4] != "http"):
                if (href[0] =="/"):
                    href = url.rstrip("/") + href
                elif (href[0] == "."):
                    href = url.rstrip("/") + href.lstrip(".")
                elif (href[:4] == "mail" or href[:3] == "tel"):
                    href = "--> " + href
                else:
                    href = "--* " + href
            print("Found hyperlink: " + href)
            hrefs.append(href)
    except:
        print("error: " + url + " not found.")
        hrefs.append("Error: Unable to crawl URL")
    return hrefs

getPage(url)