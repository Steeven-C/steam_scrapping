
#importation de toutes les lib necessaire
import requests
from bs4 import BeautifulSoup


r= requests.get("https://store.steampowered.com/stats/?l=frenc")
#print(r.status_code)
soup = BeautifulSoup(r.text,"html.parser")
#print(soup)


#soup.find_all("tbody")
game_links = soup.find_all('a',class_="gameLink")

#scrapping url list
url_list = []
for link in game_links:
    url_list.append(link.get('href'))

#getting game genre from url

for url in url_list:
    print(url)
    r= requests.get(f"{url}")
    soup = BeautifulSoup(r.text,"html.parser")
    game_genres = soup.find_all('a',class_="app_tag")
    for game_genre in game_genres:
        game_genre = game_genre.text.strip()
        print(game_genre)










    

    






