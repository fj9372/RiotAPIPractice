import operator
import time
import requests

def testMethod(name):
    api_key = "RGAPI-52ada476-c1b5-4a5b-a755-3344937a916a"
    user_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + '?api_key=' + api_key
    user = requests.get(user_url).json()

    riotID = user['id']                    
    riotAccountID = user['accountId']
    riotPuuID = user['puuid']
    riotName = user['name']
    iconID = user['profileIconId']
    level = user['summonerLevel']         

    matches_url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" + riotPuuID + '/ids?start=0&count=100&api_key=' + api_key
    
    matches = requests.get(matches_url).json()
    augment_dict = {}
    hello = 1
    for i in matches:
        time.sleep(1.5)
        tft_url = "https://americas.api.riotgames.com/tft/match/v1/matches/" + i + '?api_key=' + api_key
        match = requests.get(tft_url)
        print(match)
        match = match.json()
        print(match['metadata']['match_id'], hello)
        hello+=1
        participants = match['info']['participants']
        for participant in participants:
            if(participant['puuid'] == riotPuuID):
                for augment in participant['augments']:
                    if augment in augment_dict.keys():
                        augment_dict[augment] += 1
                    else:
                        augment_dict[augment] = 1
    sort_augment = dict(sorted(augment_dict.items(), key = operator.itemgetter(1), reverse=True))
    print(sort_augment)


