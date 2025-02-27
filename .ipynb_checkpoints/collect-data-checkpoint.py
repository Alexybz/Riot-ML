import requests
import pandas as pd

base_url = "https://na1.api.riotgames.com/lol"

riot_dev_key = "RGAPI-0faffa67-ae9f-43da-a6a3-3833ee6bc474"

def get_encrypted_summoners(mode, tier, division):
    #returns list of summoners and their information
    url = f"{base_url}/league/v4/entries/{mode}/{tier}/{division}"
    headers = {"X-Riot-Token": riot_dev_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data
    else:
        print(f"error: {response.status_code}")
        return []
    
def get_enc_summoner_id(mode, tier, division):
    #returns one encoded summoner id
    summoners = get_encrypted_summoners(mode, tier, division)
    summoner_ids = [summoner["summonerId"] for summoner in summoners]
    return summoner_ids

def get_puuid(enc_summoner_id):
    #returns puuid by encoded summoner id
    url = f"{base_url}/summoner/v4/summoners/{enc_summoner_id}"
    headers = {"X-Riot-Token": riot_dev_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        puuid = response.json()['puuid']
        return puuid
    else:
        print(f"error: {response.status_code}")
        return ""
    
    
def get_match_id(puuid, queue):
    #returns list of match_ids (str)
    #queue=490 for quickplay
    url = f"{base_url}/match/v5/matches/by-puuid/{puuid}/ids?queue={queue}"
    headers = {"X-Riot-Token": riot_dev_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        match_id_list = response.json()
        return match_id_list
    else:
        print(f"error: {response.status_code}")
        return []

def get_match_info(match_id):
    #returns all match info for one match
    url = f"{base_url}/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": riot_dev_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        match_info = response.json()
        return match_info
    else:
        print(f"error: {response.status_code}")
        return []
