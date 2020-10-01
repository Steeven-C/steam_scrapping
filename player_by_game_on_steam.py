
#importation de toutes les lib necessaire
import requests
from bs4 import BeautifulSoup

r= requests.get("https://store.steampowered.com/stats/?l=frenc")
#print(r.status_code)
soup = BeautifulSoup(r.text,"html.parser")
#print(soup)

#soup.find_all("tbody")
test = soup.find_all("tr",class_="player_count_row")
for element in test:
    toto = element.text
    print(toto)

print(len(toto))
