import requests, csv
from bs4 import BeautifulSoup

global num
global inventory
num = 0
inventory = {}


def mainCrawler(maxPages):
    page = 1
    global num
    global inventory
    while page <= maxPages:
        url = ("https://de.statista.com/statistik/suche/"
               "?accuracy=and&companies=1&itemsPerPage=3"
               "&q=Bau&subCategory=0&p=" + str(page))
        QuellCode = requests.get(url)
        QuellText = QuellCode.text
        soup = BeautifulSoup(QuellText)
        for link in soup.findAll('a', {'tabindex': '2'}):
            urlHyperlink = "https://de.statista.com/" + link['href']
            # print urlHyperlink
            getHyperlinks(urlHyperlink)
            # print(link.span)
        page += 1
        num += 1
    print inventory
    with open('test.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(inventory.items())


def getHyperlinks(itemUrl):
    global num, inventory
    Quellcode = requests.get(itemUrl)
    Quelltext = Quellcode.text
    soup = BeautifulSoup(Quelltext)
    zwires = []
    zahl = 0
    for header in soup.findAll('td'):
        if zahl % 2 != 0:
            zwires.append(header)
            # print header
        # print zwires
        zahl += 1
    print num
    print zwires
    inventory[str(num)] = zwires

# Webcrawler starten.
mainCrawler(10)
