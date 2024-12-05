from bs4 import Tag
from bs4 import BeautifulSoup

from ParseUrl import parseUrlResponse

def getAllSets():
    url = "https://www.tcgcollector.com/sets"
    soup = parseUrlResponse(url)
    if soup is not None:
        #TODO only scarlet violet?
        setSeries = soup.body.find('div', attrs={'id':'scarlet-violet-series'})
        gridItems = setSeries.find('div', attrs={'class':'set-logo-grid-items'})

        allSets = []

        for e in gridItems.children:
            if type(e) is Tag:
                setInfo = e.find('span', attrs={'class':'set-logo-grid-item-set-name-container'})
                setPath = setInfo.a['href']
                mySet = {
                    'setPath': setPath,
                    'setCode': setInfo.span.get_text(strip=True),
                    'setId': getSetIdFromPath(setPath=setPath)
                }
                allSets.append(mySet)
    return allSets

#TODO maybe make this better
def getSetIdFromPath(setPath):
    s = setPath.split('/')
    return s[2]

if __name__ == '__main__':
    for s in getAllSets():
        print("{0}\t{1}\t{2}".format(s['setCode'], s['setId'], s['setPath']))