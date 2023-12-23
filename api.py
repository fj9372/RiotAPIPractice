import requests

def testMethod(name):
    api_key = "RGAPI-dd6b6804-aa31-4306-b124-cc7b9d853021"
    user_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + '?api_key=' + api_key
    user = requests.get(user_url).json()

    riotID = user['id']                    
    riotAccountID = user['accountId']
    riotPuuID = user['puuid']
    riotName = user['name']
    iconID = user['profileIconId']
    level = user['summonerLevel']         

    matches_url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" + riotPuuID + '/ids?start=0&count=20&api_key=' + api_key
    
    mathces = requests.get(matches_url).json()

