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

# players
@app.get("/coc-api/players/{player_tag}")
def get_player(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    return make_request(final_url)

# clans
@app.get("/coc-api/clans/{clan_tag}")
def get_clan(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/%23{clan_tag}'
    return make_request(final_url)

@app.get("/coc-api/clans/{clan_tag}/currentWar/leaguegroup")
def get_clan_war_league_group(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/%23{clan_tag}/currentWar/leaguegroup'
    return make_request(final_url)

@app.get("/coc-api/clanwarleagues/wars/{war_tag}")
def get_clan_war_league_war(war_tag: str):
    final_url = f'{BASE_URL}/clanwarleagues/wars/{war_tag}'
    return make_request(final_url)

@app.get("/coc-api/{clan_tag}/warlog")
def get_clan_warlog(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/{clan_tag}/warlog'
    return make_request(final_url)

@app.get("/coc-api/clans/{clan_tag}/currentwar")
def get_clan_current_war(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/{clan_tag}/currentwar'
    return make_request(final_url)

@app.get("/coc-api/clans/{clan_tag}/members")
def get_clan_members(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/{clan_tag}/members'
    return make_request(final_url)

@app.get("/coc-api/clans/{clan_tag}/capitalraidseasons")
def get_clan_capital_raid_seasons(clan_tag: str):
    final_url = f'{BASE_URL}/{CLANS_ENDPOINT}/{clan_tag}/capitalraidseasons'
    return make_request(final_url)

# leagues
@app.get("/coc-api/capitalleagues")
def get_capital_leagues():
    final_url = f'{BASE_URL}/capitalleagues'
    return make_request(final_url)

@app.get("/coc-api/leagues")
def get_leagues():
    final_url = f'{BASE_URL}/{LEAGUES_ENDPOINT}'
    return make_request(final_url)

@app.get("/coc-api/leagues/{league_id}/seasons/{season_id}")
def get_league_season_ranking(league_id: str, season_id: str):
    final_url = f'{BASE_URL}/{LEAGUES_ENDPOINT}/{league_id}/seasons/{season_id}'
    return make_request(final_url)

@app.get("/coc-api/capitalleagues/{league_id}")
def get_capital_league(league_id: str):
    final_url = f'{BASE_URL}/capitalleagues/{league_id}'
    return make_request(final_url)

@app.get("/coc-api/builderbaseleagues/{league_id}")
def get_builder_base_league(league_id: str):
    final_url = f'{BASE_URL}/builderbaseleagues/{league_id}'
    return make_request(final_url)

@app.get("/coc-api/builderbaseleagues")
def get_builder_base_leagues():
    final_url = f'{BASE_URL}/builderbaseleagues'
    return make_request(final_url)

@app.get("/coc-api/leagues/{league_id}")
def get_league(league_id: str):
    final_url = f'{BASE_URL}/leagues/{league_id}'
    return make_request(final_url)

@app.get("/coc-api/leagues/{league_id}/seasons")
def get_league_seasons(league_id: str):
    final_url = f'{BASE_URL}/leagues/{league_id}/seasons'
    return make_request(final_url)

@app.get("/coc-api/warleagues/{league_id}")
def get_war_league(league_id: str):
    final_url = f'{BASE_URL}/warleagues/{league_id}'
    return make_request(final_url)

@app.get("/coc-api/warleagues")
def get_war_league():
    final_url = f'{BASE_URL}/warleagues'
    return make_request(final_url)

# locations
@app.get("/coc-api/locations")
def get_locations():
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}'
    response = make_request(final_url)
    locations = response['items']
    return locations

@app.get("/coc-api/locations/{location_id}/rankings/clans")
def get_clan_rankings_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/clans'
    return make_request(final_url)

@app.get("/coc-api/locations/{location_id}/rankings/players")
def get_rankings_players_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/players'
    return make_request(final_url)

@app.get("/coc-api/locations/{location_id}/rankings/players-builder-base")
def get_player_builder_base_ranking_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/players-builder-base'
    return make_request(final_url)

@app.get("/coc-api/locations/{location_id}/rankings/clans-builder-base")
def get_clan_builder_base_rankings_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/clans-builder-base'
    return make_request(final_url)

@app.get("/coc-api/locations/{location_id}/rankings/capitals")
def get_capital_rankings_by_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/rankings/capitals'
    return make_request(final_url)

@app.get("/coc-api/locations/{location_id}")
def get_location(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}'
    return make_request(final_url)

# goldpass
@app.get("/coc-api/goldpass/seasons/current")
def get_current_goldpass():
    final_url = f'{BASE_URL}/goldpass/seasons/current'
    return make_request(final_url)

# labels
@app.get("/coc-api/labels/players")
def get_players_labels():
    final_url = f'{BASE_URL}/labels/players'
    return make_request(final_url)

@app.get("/coc-api/labels/clans")
def get_clans_labels():
    final_url = f'{BASE_URL}/labels/clans'
    return make_request(final_url)


# CUSTOM API ENDPOINTS

@app.get("/coc-api/locations/{location_id}/rankings/players/fixed")
def get_rankings_players_by_location_custom(location_id: str):
    final_url = f'{BASE_URL}/{LOCATION_ENDPOINT}/{location_id}/{RANKINGS_ENDPOINT}/{PLAYERS_ENDPOINT}?limit=15'
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

@app.get("/coc-api/players/{player_tag}/achievements/home")
def get_player_home_achievements(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    player = make_request(final_url)

    if player.get('achievements') is None:
        return None
    
    home_achievements = [achievement for achievement in player['achievements'] if achievement['village'] == 'home']

    return home_achievements

@app.get("/coc-api/players/{player_tag}/achievements/builderbase")
def get_player_builder_base_achievements(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    player = make_request(final_url)

    if player.get('achievements') is None:
        return None
    
    builder_base_achievements = [achievement for achievement in player['achievements'] if achievement['village'] == 'builderBase']

    return builder_base_achievements

@app.get("/coc-api/players/{player_tag}/achievements/clancapital")
def get_player_clan_capital_achievements(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    player = make_request(final_url)

    if player.get('achievements') is None:
        return None
    
    clan_capital_achievements = [achievement for achievement in player['achievements'] if achievement['village'] == 'clanCapital']

    return clan_capital_achievements        

@app.get("/coc-api/players/{player_tag}/clan")
def get_player_clan(player_tag: str):
    final_url = f'{BASE_URL}/{PLAYERS_ENDPOINT}/%23{player_tag}'
    player = make_request(final_url)
    if player.get('clan') is None:
        return None
    return player['clan']

@app.get("/coc-api/countries")
def get_countries():
    locations = get_locations()
    countries = [location for location in locations if location['isCountry']]
    return countries
        
