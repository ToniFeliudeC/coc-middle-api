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
LEAGUES_ENDPOINT = "leagues"
CLANS_ENDPOINT = "clans"
LOCATION_ENDPOINT = "locations"
RANKINGS_ENDPOINT= "rankings"

final_url = None

HEADERS = {
    "Accept" : "application/json",
    "Authorization" : "Bearer " + key
}

def make_request(url: str):
    response = requests.get(url, headers=HEADERS)
    return response.json()

@app.get("/")
def get_root():
    return "<p>It works</p>"

@app.get("/coc-api/players/{player_tag}")
def get_player(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    return make_request(final_url)

@app.get("/coc-api/clans/{clan_tag}")
def get_clan(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/%23{clan_tag}'
    return make_request(final_url)

@app.get("/coc-api/locations")
def get_locations():
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}'
    response = make_request(final_url)
    locations = response['items']
    return locations
        
@app.get("/coc-api/locations/{location_id}/rankings/players")
def get_rankings_players_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/{RANKINGS_ENDPOINT}/{PLAYERS_ENDPOINT}'
    response = make_request(final_url)
    players = response['items']
    return players