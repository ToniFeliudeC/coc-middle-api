from fastapi import FastAPI
import requests
from api_key import key
from fastapi.middleware.cors import CORSMiddleware
import logging

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

# OFFICIAL API ENDPOINTS DUPLICATES

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

# CUSTOM API ENDPOINTS

@app.get("/coc-api/locations/{location_id}/rankings/players")
def get_rankings_players_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/{RANKINGS_ENDPOINT}/{PLAYERS_ENDPOINT}?limit=10'
    response = make_request(final_url)
    players = response['items']

    for player in players:
        player_clan = get_player_clan(player['tag'][1:])
        if player_clan is not None:
            try:
                player['clan']['badgeUrls'] = player_clan['badgeUrls']
            except:
                pass
    return players

@app.get("/coc-api/players/{player_tag}/clan")
def get_player_clan(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    player = make_request(final_url)
    if player.get('clan') is None:
        return None
    return player['clan']

@app.get("/coc-api/countries")
def get_countries():
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}'
    response = make_request(final_url)
    locations = response['items']
    countries = [location for location in locations if location['isCountry']]
    return countries
        
