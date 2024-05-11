from fastapi import FastAPI
import requests
from api_key import key
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://api.clashofclans.com/v1"
PLAYERS_ENDPOINT = "players"
LEAGUES_ENDPOINT = "leagues/"
CLANS_ENDPOINT = "clans"
LOCATION_ENDPOINT = "locations"

final_url = None

headers = {
    "Accept" : "application/json",
    "Authorization" : "Bearer " + key
}

@app.get("/")
def get_root():
    return "<p>It works</p>"

@app.get("/coc-api/players/{player_tag}")
def get_player(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data

@app.get("/coc-api/clans/{clan_tag}")
def get_clan(clan_tag: str):
    final_url = f'{BASE_URL}/clans/%23{clan_tag}'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data

@app.get("/coc-api/locations/{location_id}/rankings/players")
def get_location_ranking_list(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/players'
    response = requests.get(final_url, headers=headers)
    data = response.json()
    return data