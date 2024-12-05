from bs4 import Tag
from bs4 import BeautifulSoup

from ParseUrl import parseUrlResponse

def getAllCardsInSet(setId):
    url = "https://www.tcgcollector.com/sets/{0}".format(setId)

    soup = parseUrlResponse(url)
    if soup is not None:
        cards = soup.body.find('div', attrs={'id':'card-image-grid'})

        allCards = []

        for e in cards.children:
            if type(e) is Tag:
                cardId = e['data-card-id']
                cardNumber = e.find('span', attrs={'class': 'card-image-grid-item-info-overlay-text-part'}).get_text(strip=True)
                card = {
                    'cardId': cardId,
                    'cardNumber': cardNumber
                }
                allCards.append(card)

        return allCards


if __name__ == '__main__':
    setId = 11507
    for c in getAllCardsInSet(setId=setId):
        print("https://www.tcgcollector.com/cards/{0} {1}".format(c['cardId'], c['cardNumber']))