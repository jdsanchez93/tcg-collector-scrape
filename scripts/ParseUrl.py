from bs4 import BeautifulSoup
import requests

def parseUrlResponse(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    return None