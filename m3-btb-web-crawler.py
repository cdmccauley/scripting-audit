#
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