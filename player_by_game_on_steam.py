
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
    #Selecting players pike
    game_activity = game_activity.text
    players_pike = (" ".join((game_activity).split())).split()[1]
    print(f"pic de joueurs : {players_pike}")
    #Selecting game name
    liste = (" ".join((game_activity).split()))
    liste= liste.split()
    game = liste
    del game[0:2]
    game = " ".join(game)
    print(f"jeu : {game}")
    print("----------------------------------------------------------------------------------------")



#scrapping total steam_player
steam_player = soup.find("span", class_="statsTopHi").text
print(f"total steam players : {steam_player}")

