# import libraries
from typing import Any
import requests
import matplotlib.pyplot as plt
import json

api_key = input("Please enter your API key:  ")
user_id = input("Please enter your steamID:  ")
steam_req = input("What kind of request would you like to make ? \n [1] for Game news \n [2] for Hours played graph, by game \n :  ")

steam_req = int(steam_req)

def send_req(url):
    response = requests.get(url)
    data = response.json()
    return data

def game_news(key):
    game_id = input("Please enter the game ID of the game you would like to see:  ")
    # add a new input for number of items?
    url = f"http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={game_id}&count=5&maxlength=500&format=json"
    data = send_req(url)

    # Print the JSON response
    print(json.dumps(data, indent=4))

def game_graph(api, user):
    url = f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001?key={api}&steamid={user}&format=json"
    data = send_req(url)
    
    if data:
        # Extract relevant data from the response
        games = [game["name"] for game in data["response"]["games"]]
        hours_played = [game["playtime_forever"] for game in data["response"]["games"]]

        # Plot the bar graph
        plt.bar(games, hours_played)
        plt.xlabel("Game")
        plt.ylabel("Hours Played")
        plt.title("Hours Played per Game")
        plt.xticks(rotation=90)
        plt.show()
if steam_req == 1:
    game_news(api_key)
if steam_req == 2:
    game_graph(api_key, user_id)
else:
    print("You selected option 2")



# # Send API request
# response = requests.get("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001?key=3BBDF0A22681BDA6FA692BC17D02392F&steamid=76561198415081065&format=json")
# data = response.json()
#
