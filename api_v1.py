import requests
import matplotlib.pyplot as plt

# Send API request
response = requests.get("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001?key=3BBDF0A22681BDA6FA692BC17D02392F&steamid=76561198415081065&format=json")
data = response.json()

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
