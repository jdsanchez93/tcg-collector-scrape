from GetSets import getAllSets
from GetCardsForSet import getAllCardsInSet
import json

def getTotalCards(cardNumber):
    if '/' in cardNumber:
        return int(cardNumber.split('/')[1])
    return 0

if __name__ == '__main__':
    allSets = getAllSets()
    for s in allSets:
        allCards = getAllCardsInSet(setId=s['setId'])
        cardNumber = allCards[0]['cardNumber']
        s['totalCards'] = getTotalCards(cardNumber=cardNumber)
        s['cards'] = allCards
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(allSets, f)