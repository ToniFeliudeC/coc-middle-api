from fastapi import FastAPI
import requests
from api_key import key

app = FastAPI()

base_url = "https://api.clashofclans.com/v1"
players_endpoint = "players"
leagues_endpoint = "leagues/"
clans_endpoint = "clans"
location_endpoint = "locations"
final_url = None

headers = {
    "Accept" : "application/json",
    "Authorization" : "Bearer " + key
}

@app.get("/coc-api/players/{player_tag}")
def get_player(player_tag: str):
    final_url = f'{base_url}/{players_endpoint}/%23{player_tag}'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data

@app.get("/coc-api/clans/{clan_tag}")
def get_player(clan_tag: str):
    final_url = f'{base_url}/clans/%23{clan_tag}'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data

@app.get("/coc-api/locations/{location_id}/rankings/players")
def get_player(location_id: str):
    final_url = f'{base_url}/{location_endpoint}/{location_id}/rankings/players'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data