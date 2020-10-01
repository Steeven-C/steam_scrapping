# je suis une fougère
#importation de toutes les lib necessaire
import requests
from bs4 import BeautifulSoup

r= requests.get("https://store.steampowered.com/stats/?l=frenc")
#print(r.status_code)
soup = BeautifulSoup(r.text,"html.parser")
#print(soup)

#soup.find_all("tbody")
game_activities = soup.find_all("tr",class_="player_count_row")
for game_activity in game_activities:
    game_activity = game_activity.text
    print(game_activity)


steam_player = soup.find("span", class_="statsTopHi").text
print(steam_player)
